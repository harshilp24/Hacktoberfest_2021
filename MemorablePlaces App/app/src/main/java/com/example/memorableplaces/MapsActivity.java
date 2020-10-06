package com.example.memorableplaces;

import androidx.annotation.NonNull;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import androidx.fragment.app.FragmentActivity;

import android.Manifest;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.Toast;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback,GoogleMap.OnMapLongClickListener {

    LocationManager locationManager;
    LocationListener locationListener;
    private GoogleMap mMap;
    static ArrayList<LatLng> locations=new ArrayList<LatLng>();
    String ag= "";
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if(grantResults.length!=0 && grantResults[0]==PackageManager.PERMISSION_GRANTED){
            if(ContextCompat.checkSelfPermission(this,Manifest.permission.ACCESS_FINE_LOCATION)==PackageManager.PERMISSION_GRANTED){
                locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,0,0,locationListener);
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

    }

    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap ) {
        Intent init = getIntent();
        int a=init.getIntExtra("IDK",999);
        mMap = googleMap;
        if (a==999) {
            mMap.setOnMapLongClickListener(this);
        }
        else{
            LatLng latLng = new LatLng(locations.get(a).latitude,locations.get(a).longitude);
            mMap.addMarker(new MarkerOptions().position(latLng).title("Marker in Sydney"));
            mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(latLng,10));
            MainActivity.adapter.notifyDataSetChanged();
        }


        // Add a marker in Sydney and move the camera
        locationManager = (LocationManager) this.getSystemService(LOCATION_SERVICE);
        locationListener = new LocationListener() {
            @Override
            public void onLocationChanged(@NonNull final Location location1) {
                if(locations.size()==0) {
                    mMap.clear();
                    LatLng dyh = new LatLng(location1.getLatitude(), location1.getLongitude());
                    mMap.addMarker(new MarkerOptions().position(dyh).title("Marker in Sydney"));
                    mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(dyh, 12));
                }
                else{
                    Toast.makeText(MapsActivity.this, "", Toast.LENGTH_SHORT).show();
                }
            }
            @Override
            public void onStatusChanged(String s, int i, Bundle bundle) {

            }

            @Override
            public void onProviderEnabled(String s) {

            }

            @Override
            public void onProviderDisabled(String s) {

            }
        };


        SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        int dha;
        dha= prefs.getInt("iDK",999);
        if(ContextCompat.checkSelfPermission(this,Manifest.permission.ACCESS_FINE_LOCATION)!= PackageManager.PERMISSION_GRANTED){
            ActivityCompat.requestPermissions(this,new String[] {Manifest.permission.ACCESS_FINE_LOCATION},1);
            Location lastKnownLocation = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            LatLng lat=new LatLng(lastKnownLocation.getLatitude(),lastKnownLocation.getLongitude());
            mMap.addMarker(new MarkerOptions().position(lat).title("Marker in Sydney"));
            mMap.moveCamera(CameraUpdateFactory.newLatLng(lat));
        }else{
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,0,0,locationListener);
        }


    }
    @Override
    public void onMapLongClick(LatLng latLng) {
        locations.add(latLng);
        mMap.addMarker(new MarkerOptions().position(latLng).title("Marker in Sydney"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(latLng));
        try {
            Geocoder geocoder = new Geocoder(getApplicationContext(), Locale.getDefault());
            List<Address> list = geocoder.getFromLocation(latLng.latitude, latLng.longitude, 1);
            if (list != null && list.size() != 0) {
                if (list.get(0).getThoroughfare() != null) {
                    ag += list.get(0).getThoroughfare() + " ";
                }
                if (list.get(0).getSubAdminArea() != null) {
                    ag += list.get(0).getSubAdminArea() + " ";
                }
                if (list.get(0).getAdminArea() != null) {
                    ag += list.get(0).getAdminArea() + " ";

                }
            } else {
                ag = "No Address Gomene";
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        Toast.makeText(MapsActivity.this, ag, Toast.LENGTH_LONG).show();
        MainActivity.dha.add(ag);
        MainActivity.adapter.notifyDataSetChanged();
        finish();

    }
}