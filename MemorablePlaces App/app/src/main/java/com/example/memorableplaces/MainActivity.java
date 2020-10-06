package com.example.memorableplaces;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {
    ListView lw;
    static ArrayList<String> dha=new ArrayList<String>();
    static ArrayList<Integer> dhaaa=new ArrayList<Integer>();
    static ArrayAdapter<String> adapter;
    public void main(View view){
        Intent dhaa = new Intent(getApplicationContext(),MapsActivity.class);
        if (dhaa.getStringExtra("Address")!=null){
            dha.add(dhaa.getStringExtra("Address"));
        }
        startActivity(dhaa);
        lw = findViewById(R.id.Yay);
        lw.setAdapter(adapter);
        lw.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Intent in = new Intent(getApplicationContext(),MapsActivity.class);
                in.putExtra("IDK",i);
                startActivity(in);
            }
        });
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if(dha.size()==0){
            adapter= new ArrayAdapter<String>(this,android.R.layout.simple_list_item_1,dha);
        }
    }
}