![](/src/data/icon.png)

# askyourself

App that asks you important questions

## build
1. make debug
2. put 
```
<receiver android:name="org.atq.atq.TaskReceiver" android:enabled="true" android:exported="true" />
```
to `.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/sdl2/build/templates/AndroidManifest.tmpl.xml`
3. put
```
        //foreground: {{foreground}}
        {% if foreground %}
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            ctx.startForegroundService(intent);
        } else {
            ctx.startService(intent);
        }
        {% else %}
        ctx.startService(intent);
        {% endif %}
```
to `.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/common/build/templates/Service.tmpl.java`