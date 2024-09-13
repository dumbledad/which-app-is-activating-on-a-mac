# Which App is Activating on a Mac?

Recently the app I am typing into on my Mac randomly loses focus. This may help find out why.

The code is copied from [Mike Edmunds](https://github.com/medmunds) answer to the superuser question [How do I tell which app stole my focus in OS X?](https://superuser.com/a/874314/166855).

## Results

This worked a treat for me and clearly pointed to the culprit:

```text
2024-09-13 09:35:33: Google Chrome [/Applications/Google Chrome.app]
2024-09-13 09:38:52: platform-communicator-tray [/Applications/platform-communicator-tray.app]
2024-09-13 09:38:57: iTerm2 [/Applications/iTerm.app]
```

It could be that `platform-communicator-tray.app` has not coped with the removal of my day-to-day account's admin privileges.