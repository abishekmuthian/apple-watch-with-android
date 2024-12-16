# Sync contacts from android to Apple Watch

With this setup we'll sync contacts from Android to iOS on iPhone with which the apple watch is paired. Then with a cellular Apple Watch we need not carry the iPhone with us.

## Requirements

1. [Nextcloud](https://nextcloud.com/) server.
2. Nextcloud client app on Android.
3. [Davx](https://www.davx5.com/) on Android.
4. CardDAV supported android contacts app, I use default AOSP contacts app.
5. iPhone and Apple Watch paired with it.

## How To

1. Setup or get a Nextcloud server instance.
2. Follow the [Sync with Android guide](https://docs.nextcloud.com/server/30/user_manual/en/groupware/sync_android.html#contacts-and-calendar).
3. Follow the [Sync with iOS guide](https://docs.nextcloud.com/server/30/user_manual/en/groupware/sync_ios.html#contacts).

When done successfully all the contacts from android will be synced in real-time with iOS and thereby on Apple Watch OS.

## Demo

![Contacts app on Apple Watch](./contacts-apple-watch.png)
