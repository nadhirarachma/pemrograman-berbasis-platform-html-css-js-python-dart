import 'package:accounts/screens/login_screen.dart';
import 'package:accounts/utils/drawer_screen.dart';
import 'package:accounts/utils/network_service.dart';
import 'package:flutter/material.dart';
import 'package:healthy_advice/screens/healthy_advice_home.dart';
import 'package:provider/provider.dart';
import 'package:accounts/screens/welcome_screen.dart';
import 'package:accounts/constants.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.

  @override
  Widget build(BuildContext context) {
    return Provider(
      create: (_) {
        NetworkService request = NetworkService();
        return request;
      },
      child: MaterialApp(
        title: "E-Nadi Login",
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
            primaryColor: kPrimaryColor, scaffoldBackgroundColor: Colors.white),
        home: const WelcomeScreen(),

        routes: {
          HealthyAdviceHome.routeName: (context) => const HealthyAdviceHome(title: 'e-nadi Healthy Advice'),
          LoginScreen.routeName : (context) => const LoginScreen(),
          HomeDummy.routeName : (context) => const HomeDummy(),

        },
      ),
    );
  }
}

class HomeDummy extends StatefulWidget {
  static const routeName = '/homedummy';
  const HomeDummy({Key? key}) : super(key: key);

  @override
  _HomeDummyState createState() => _HomeDummyState();
}

class _HomeDummyState extends State<HomeDummy> {
  @override
  Widget build(BuildContext context) {
    final request = context.watch<NetworkService>();
    return Scaffold(
        appBar: AppBar(
          title: const Text("Home Dummy"),
        ),
        drawer: request.username != "" ? const DrawerScreen() : const DrawerScreen(),
        body:
        Container(

        )
    );
  }
}

