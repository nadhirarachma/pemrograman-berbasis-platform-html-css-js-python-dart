import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:lab_7/screens/summary.dart';

class MainDrawer extends StatelessWidget {
  Widget buildListTile(String title, IconData icon, Function() tapHandler) {
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
      onTap: tapHandler,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Container(
        color: Colors.grey[900],
        child: Column(
          children: <Widget>[
            Container(
              height: 120,
              width: double.infinity,
              padding: EdgeInsets.all(20),
              alignment: Alignment.centerLeft,
              color: Colors.black,
              child: Text(
                'e-Nadi',
                style: TextStyle(
                    fontWeight: FontWeight.w900,
                    fontSize: 30,
                    color: Colors.red),
              ),
            ),
            SizedBox(
              height: 20,
            ),
            buildListTile('Home', Icons.home, () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ActivitySummaryApp()));
            }),
            buildListTile('Workout Tracker', Icons.fitness_center, () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ActivitySummaryApp()));
            }),
            buildListTile('Sleep Tracker', Icons.bed, () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ActivitySummaryApp()));
            }),
            buildListTile('Recipe', Icons.food_bank, () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ActivitySummaryApp()));
            }),
            buildListTile('Activity Summary', Icons.people, () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ActivitySummaryApp()));
            }),
            buildListTile('Healthy Advice', Icons.health_and_safety, () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ActivitySummaryApp()));
            }),
            buildListTile('Login/Register', Icons.settings, () {
              Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ActivitySummaryApp()));
            }),
          ],
        ),
      ),
    );
  }
}
