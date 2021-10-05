import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;
import java.util.Timer;
import java.util.TimerTask;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.joda.time.DateTime;
import org.joda.time.Period;
import org.joda.time.format.DateTimeFormat;
import org.joda.time.format.DateTimeFormatter;

import upm_grove.GroveButton;
import upm_grove.GroveRotary;
import mraa.Platform;
import mraa.mraa;

import com.google.gson.Gson;

public class AlarmClock {

	private static Properties config = new Properties();
	private static AlarmLcd lcdScreen;
	private static AlarmBuzzer buzzer;
	private static GroveRotary rotary;
	private static float lastRotary = -1;
	private static GroveButton button;
	private static DateTime currentTime = new DateTime();
	private static DateTime alarmTime;
	private static Timer alarmTimerObj = new Timer();
	private static boolean alarmActive = false;
	private static boolean tick = true;

	public static void initSensors(){
		lcdScreen = new AlarmLcd();
		buzzer = new AlarmBuzzer(5);
		rotary = new GroveRotary(0);
		button = new GroveButton(4);
	}
	
	public static void startClock() {
		Timer clockTimer = new Timer();
		DateTimeFormatter dateFormat = DateTimeFormat.forPattern("H:mm:ss a");
		clockTimer.schedule(new TimerTask() {
			public void run() {
				DateTime date = new DateTime();
				if (date.isAfter(currentTime)){
					lcdScreen.displayMessageOnLcd(dateFormat.print(date) ,0);
					if (alarmTime != null && !alarmActive){
						if ((currentTime.withMillisOfSecond(0)).isEqual(alarmTime.withMillisOfSecond(0))) 
							startAlarm();
					}
				}
				currentTime = date;
			}
		}, 50,50);
	}
	
	private static void startAlarm() {
		lcdScreen.setLcdColor("red");	
		buzzer.buzz();
		String weather = "";
		try {
			weather = Utils.getWeather(config)//get weather of location set in config file
		} catch (IOException e) {
			System.out.println("unable to get weather data");
			e.printStackTrace();
		}
		lcdScreen.displayMessageOnLcd(weather, 1);
		alarmActive = true;
		alarmTimerObj.schedule(new TimerTask() {
			public void run() {
				lcdScreen.setLcdColor(tick ? "white" : "red");
				if (tick){ 
					buzzer.stopBuzzing(); 
				} 
				else { 
					buzzer.buzz(); 
				}
				tick = !tick;
			}
		}, 250, 250);
	}
  
	public static void checkSensorsActivity() {
		Timer activityCheckTimer = new Timer();
		activityCheckTimer.schedule(new TimerTask() {
			public void run() {
				if (rotary.abs_value() != lastRotary){
					lastRotary = rotary.abs_value();
					lcdScreen.adjustBrightness(lastRotary);
				}
			}
		}, 100,100);
		
		button.installISR(2,new Runnable() {
			
			@Override
			public void run() {
				System.out.println("button clicked");
				alarmTimerObj.cancel();
				alarmTimerObj = new Timer();
				Period interval = new Period(alarmTime, (new DateTime())); 
				Utils.notifyAzure(String.valueOf(interval.toDurationFrom(new DateTime()).getMillis()), config);
				
				alarmTime.plusDays(1);
				lcdScreen.setLcdColor("white");
				buzzer.stopBuzzing();
				alarmActive = false;
			}
		});
	}
	
	public static void setupServer() {
		ServerSetup server= new ServerSetup();
		server.setupServer(8080);
		server.addServlet("/", new ServerSetup.GetCall(){
			@Override
			public void runCall(HttpServletRequest request, HttpServletResponse response) throws IOException {
				if (request.getRequestURI().matches("/")){
					Map<String, String[]> params = request.getParameterMap();
					DateTime time = new DateTime();
					if (params.containsKey("hour")&& params.containsKey("minute")&&params.containsKey("second")){
						time = time.withTime(Integer.parseInt(request.getParameter("hour")),
								Integer.parseInt(request.getParameter("minute")), 
								Integer.parseInt(request.getParameter("second")),
								0);
						if (time.isBefore(new DateTime())){
							time.plusDays(1);
						}		
						alarmTime = time;
					}
					String sCurrentLine;
					@SuppressWarnings("resource")
					BufferedReader indexFile = new BufferedReader(new FileReader("/var/AlarmClock/index.html"));
					StringBuilder stringBuilder = new StringBuilder();
					while ((sCurrentLine = indexFile.readLine()) != null) {
						stringBuilder.append(sCurrentLine).append("\n");
					}
					response.getWriter().println(stringBuilder.toString());
				}
			}  
		});
    
		server.addServlet("/alarm.json", new ServerSetup.GetCall(){
			public void runCall(HttpServletRequest request, HttpServletResponse response) throws IOException {
				Map<String, Integer> alarmMap = new HashMap<String, Integer>();
				if (alarmTime != null){
					alarmMap.put("hour", alarmTime.getHourOfDay());
					alarmMap.put("minute", alarmTime.getMinuteOfHour());
					alarmMap.put("second", alarmTime.getSecondOfMinute());
				}
				else{
					alarmMap.put("hour", 0);
					alarmMap.put("minute", 0);
					alarmMap.put("second", 0);
				}
        
				response.setContentType("application/json");
				response.setStatus(HttpServletResponse.SC_OK);
				Gson gson = new Gson();
				String result =gson.toJson(alarmMap);
				response.getWriter().println(result);
			}  
		});

		server.run();
	}

	public static void main(String[] args) {
		Platform platform = mraa.getPlatformType();
		if (platform != Platform.INTEL_GALILEO_GEN1 &&
				platform != Platform.INTEL_GALILEO_GEN2 &&
				platform != Platform.INTEL_EDISON_FAB_C) {
			System.err.println("Unsupported platform, exiting");
			return;
		}
		try {
			config.load(AlarmClock.class.getClassLoader().getResourceAsStream("config.properties"));
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		initSensors();
		buzzer.stopBuzzing();
		startClock();
		checkSensorsActivity();
		setupServer();
	}
}
