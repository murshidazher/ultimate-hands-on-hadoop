# Setting an admin account password and reset

Go to ssh and access root, and put in the following command

```sh
ambari-admin-password-reset
```

- You can edit the config files straight from ambari ui
- You can access the hosts to see what components are running and if it has hung, go there to restart the specific component
- Go to Alerts and you can manually set up an alert for the service, e.g enable service for HDFS Storage capacity
- You can also manage notifications for how your alerts is going to alert you
- Go inside Admin and you can see what service and version is installed inside your Hadoop stack
- You can also go inside the different files view like Hive, Pig and Yarn View 
