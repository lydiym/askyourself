package org.atq.atq;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.app.PendingIntent;
import android.app.AlarmManager;


public class TaskScheduler{
    Context appContext;

    public TaskScheduler(Context context){
        this.appContext = context;
    }

    public void scheduleTask(long taskTimeInMillis){
        AlarmManager alarmManager = (AlarmManager) appContext.getSystemService(Context.ALARM_SERVICE);

        Intent intent = new  Intent(appContext, TaskReceiver.class);

        PendingIntent pendingIntent = PendingIntent.getBroadcast(appContext, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT);
        alarmManager.setExact(AlarmManager.RTC, taskTimeInMillis, pendingIntent);
    }
}