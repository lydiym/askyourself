package org.atq.atq;

import android.content.Context;
import android.content.Intent;
import android.content.BroadcastReceiver;
import android.media.MediaPlayer;
import android.provider.Settings;
import android.os.Bundle;

public class TaskReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent){
    	arguments = ""
        ServiceNotifier.start(context, arguments);
    }

}