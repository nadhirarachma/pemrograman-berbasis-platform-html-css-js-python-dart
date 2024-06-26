import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:lab_6/screens/summary.dart';
import 'package:lab_6/screens/tabs_screen.dart';

class MainDrawer extends StatelessWidget {
  Widget buildListTile(String title, IconData icon, Function tapHandler) {
    return ListTile(
      leading: Icon(
        icon,
        size: 22,
        color: Colors.white,
      ),
      title: Text(
        title,
        style: TextStyle(
          fontFamily: 'RobotoCondensed',
          fontSize: 18,
          fontWeight: FontWeight.bold,
          color: Colors.white,
        ),
      ),
      onTap: () => ActivitySummaryApp(),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Column(
        children: <Widget>[
          Container(
            height: 120,
            width: double.infinity,
            padding: EdgeInsets.all(20),
            alignment: Alignment.centerLeft,
            color: Theme.of(context).accentColor,
            child: Text(
              'e-Nadi',
              style: TextStyle(
                  fontWeight: FontWeight.w900, fontSize: 30, color: Colors.red),
            ),
          ),
          SizedBox(
            height: 20,
          ),
          buildListTile('Home', Icons.home, () {
            Navigator.of(context).pushReplacementNamed('/');
          }),
          buildListTile('Workout Tracker', Icons.fitness_center, () {
            Navigator.of(context).pushReplacementNamed('/');
          }),
          buildListTile('Sleep Tracker', Icons.bed, () {
            Navigator.of(context).pushReplacementNamed('/');
          }),
          buildListTile('Recipe', Icons.food_bank, () {
            Navigator.of(context).pushReplacementNamed('/');
          }),
          buildListTile('Activity Summary', Icons.people, () {
            Navigator.of(context).pushReplacementNamed('/');
          }),
          buildListTile('Healthy Advice', Icons.health_and_safety, () {
            Navigator.of(context).pushReplacementNamed('/');
          }),
          buildListTile('Login/Register', Icons.settings, () {
            Navigator.of(context).pushReplacementNamed('/');
          }),
        ],
      ),
    );
  }
}
