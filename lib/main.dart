import 'package:flutter/material.dart';
import 'package:kar_zar/networking/shared_preferences.dart';
import 'package:kar_zar/web/web_main.dart';
import 'package:kar_zar/mobile/mobile_main.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await UserSharedPreferences.init();
  runApp(
    const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: KarZar(),
    ),
  );
}

class KarZar extends StatelessWidget {
  const KarZar({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    double? width = MediaQuery.of(context).size.width;
    if (width <= 566) {
      return const MobileMain();
    } else {
      return const WebMain();
    }
  }
}
