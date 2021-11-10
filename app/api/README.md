# COMO USAR ESTE API PARA MANDAR NOTIFICACOA PARA APLICATIVO SPAR:
```dart
 import 'dart:convert';
import 'dart:isolate';

import 'package:dio/dio.dart';

void sendNotificationToApi(
    {required String message,
    required String title,
    bool istoapi = false}) async {
  var uri = 'http://localhost:5000/spar/postproduct/';
  if (istoapi) {
    uri = 'http://saidinosecondapp.herokuapp.com/spar/postproduct/';
  } else {
    uri = 'https://fcm.googleapis.com/fcm/send';
  }
  final auth =
      'key=AAAAT7I801w:APA91bFyk0q5leLPRR8YtKy3Q1s1wA38IcLdhZbkXF3ysCY7HdwOZ2IJEMQoaO8t5zKTwE_A8hockdmrL1FgkKkbqfK6FX4eCP5R7o1XLliD-e3OYFY1aruXPxac9rc_x6Dr6ly17nER';
// content_type='application/json'

  var data = {
    "to": '/topics/ADMIN',
    "notification": {
      "title": title,
      "body": message,
      "image":
          "https://vipspar.com/wp-content/uploads/2020/08/33401-480x480.jpg",
    }
  };
  var response = await Dio().post(uri,
      data: jsonEncode(data),
      options: Options(headers: {
        'Content-Type': 'application/json',
        'Authorization': auth,
      }));
  print(response.data);
}

void sendToapi(
    {required String message,
    required String title,
    required String image,
    bool istoapi = false}) async {
  var uri = 'http://localhost:5000/spar/postproduct/';
  var notification = {
    "to": '/topics/ADMIN',
    "body": message,
    "title": title,
    "image": image
  };
  try {
    final response = await Dio().post(
      uri,
      data: jsonEncode(notification),
    );
  } catch (e) {}
}


```
