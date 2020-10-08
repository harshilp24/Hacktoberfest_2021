using System;
using System.IO;
using System.Collections.Generic;
using System.Text;

namespace SpeedTypingTestConsole
{
    class Program
    {
        private static double average { get; set; } = 0;
        private static TimeSpan timeTaken { get; set; }
        private static List<string> words = new List<string>();
        private static string path = AppDomain.CurrentDomain.BaseDirectory;
        private static Random random = new Random();

        static void Main(string[] args) => MenuStart();

        private static void MenuStart()
        {
            //Hook up ProcessExit to save average when exiting
            AppDomain.CurrentDomain.ProcessExit += new EventHandler(SaveAverage);

            //All of this is just so that you can add custom words to this but
            //if the file isn't found it will create it with the basic words
            try { LoadWordsFile(); }
            catch(FileNotFoundException)
            {
                CreateWordsFile();
                LoadWordsFile();
            }

            //Load average spelling time, ignore if average.txt doesn't exist
            try { LoadAverage(); }
            catch(FileNotFoundException){}

            Console.Clear();
            Console.WriteLine("PRESS ANY KEY TO START THE TEST");
            Console.WriteLine("AVERAGE TIME TAKEN: {0} SECONDS", average);
            Console.ReadKey();
            StartTypingTest();
        }

        private static void NextTestMenu()
        {
            //Writing over previous to minimize flickering
            Console.SetCursorPosition(0,0);
            Console.WriteLine("TIME TAKEN ON LAST WORD: {0} SECONDS", Math.Round(timeTaken.TotalSeconds,2));
            Console.WriteLine("AVERAGE TIME TAKEN: {0} SECONDS", average);
            Console.WriteLine("PRESS SPACE FOR NEXT TEST");
            Console.WriteLine("PRESS ENTER TO EXIT");
            switch(Console.ReadKey().Key)
            {
                case ConsoleKey.Enter:
                    break;

                case ConsoleKey.Spacebar:
                    StartTypingTest();
                    break;

                default:
                    NextTestMenu();
                    break;
            }
        }

        private static void StartTypingTest()
        {
            var timeOfStart = DateTime.Now.ToLocalTime();
            char input = ' ';
            var typed = new StringBuilder();
            var chosenWord = words[random.Next(0, words.Count)];
            
            Console.Clear();
            foreach(var letter in chosenWord)
            {
                DrawTypingText(chosenWord, typed.ToString());
                //Takes letters and deletes them from the console
                while(letter != input)
                {
                    input = Console.ReadKey().KeyChar;
                    DrawTypingText(chosenWord, typed.ToString());
                }
                typed.Append(letter);
            }
            DrawTypingText(chosenWord, typed.ToString());

            timeTaken = DateTime.Now.ToLocalTime() - timeOfStart;
            average = average == 0 ? Math.Round(timeTaken.TotalSeconds, 2) : Math.Round((average + timeTaken.TotalSeconds)/2, 2);
            Console.Clear();
            NextTestMenu();
        }

        private static void DrawTypingText(string chosenWord, string typed)
        {
            //Writing over previous to minimize flickering
            Console.SetCursorPosition(0,0);
            Console.WriteLine("TYPE: {0}", chosenWord);
            Console.Write("TYPED: {0}", typed);
        }

        private static void LoadWordsFile()
        {
            using(var streamReader = new StreamReader(path+"words.txt"))
            {
                string line;
                while((line = streamReader.ReadLine()) != null)
                    words.Add(line);
            }
        }

        private static void CreateWordsFile()
        {
            string[] basicWords = {"unciform", "shaped", "like", "hook", "rare", "repeat", "fix", "shell", "hacktober", "side"};

            using(var streamWriter = new StreamWriter(path+"words.txt"))
            {
                foreach(var word in basicWords)
                    streamWriter.WriteLine(word);
            }
        }

        private static void LoadAverage()
        {
            using(var streamReader = new StreamReader(path+"average.txt"))
            {
                average = double.Parse(streamReader.ReadLine());
            }
        }

        private static void SaveAverage(object sender, EventArgs e)
        {
            using(var streamWriter = new StreamWriter(path+"average.txt"))
            {
                streamWriter.WriteLine(average);
            }
        }
    }
}
