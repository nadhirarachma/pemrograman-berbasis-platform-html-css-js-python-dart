import 'package:flutter/material.dart';

import '../widgets/main_drawer.dart';

class EditProfileApp extends StatelessWidget {
  static const routeName = '/edit_profile';
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Activity Summary',
      theme: ThemeData(
          appBarTheme: AppBarTheme(
        color: const Color(0xFF000000),
      )),
      home: EditApp(),
    );
  }
}

class EditApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [Colors.black12, Colors.black38]),
                image: DecorationImage(
                  image: AssetImage("lib/assets/images/bg4.jpg"),
                  fit: BoxFit.cover,
                ),
              ),
              width: double.infinity,
              height: 1200,
              child: Center(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    SizedBox(
                      height: 40.0,
                    ),
                    Text(
                      "HELLO, NADHIRA!",
                      style: TextStyle(
                        fontSize: 20.0,
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(
                      height: 10.0,
                    ),
                    Text(
                      "Edit Your Profile",
                      style: TextStyle(
                        fontSize: 18.0,
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(
                      height: 10.0,
                    ),
                    Text(
                      "---------------------",
                      style: TextStyle(
                        fontSize: 18.0,
                        color: Colors.yellow[700],
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    SizedBox(
                      height: 15.0,
                    ),
                    Container(
                      child: Card(
                        margin: EdgeInsets.symmetric(
                            horizontal: 50.0, vertical: 5.0),
                        clipBehavior: Clip.antiAlias,
                        color: Color.fromRGBO(242, 248, 243, 0.5),
                        elevation: 5.0,
                        child: Padding(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 8.0, vertical: 22.0),
                          child: Row(
                            children: <Widget>[
                              Expanded(
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.center,
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: <Widget>[
                                    SizedBox(
                                      height: 10.0,
                                    ),
                                    CircleAvatar(
                                      backgroundColor: Colors.black,
                                      radius: 45.0,
                                    ),
                                    SizedBox(
                                      height: 30.0,
                                    ),
                                    TextFormField(
                                        decoration: InputDecoration(
                                      labelText: "USERNAME",
                                      hintText: 'Nadhira',
                                      labelStyle: TextStyle(
                                        fontSize: 18,
                                        fontWeight: FontWeight.bold,
                                        color: Colors.white,
                                      ),
                                      floatingLabelBehavior:
                                          FloatingLabelBehavior.always,
                                      hintStyle: TextStyle(
                                        fontSize: 14,
                                        color: Colors.black,
                                      ),
                                      contentPadding: EdgeInsets.fromLTRB(
                                          20.0, 15.0, 20.0, 15.0),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(32.0)),
                                    )),
                                    SizedBox(
                                      height: 20.0,
                                    ),
                                    TextFormField(
                                        decoration: InputDecoration(
                                      labelText: "GENDER (M/F)",
                                      hintText: 'Female',
                                      labelStyle: TextStyle(
                                        fontSize: 18,
                                        fontWeight: FontWeight.bold,
                                        color: Colors.white,
                                      ),
                                      floatingLabelBehavior:
                                          FloatingLabelBehavior.always,
                                      hintStyle: TextStyle(
                                        fontSize: 14,
                                        color: Colors.black,
                                      ),
                                      contentPadding: EdgeInsets.fromLTRB(
                                          20.0, 15.0, 20.0, 15.0),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(32.0)),
                                    )),
                                    SizedBox(
                                      height: 20.0,
                                    ),
                                    TextFormField(
                                        decoration: InputDecoration(
                                      labelText: "AGE",
                                      hintText: '19',
                                      labelStyle: TextStyle(
                                        fontSize: 18,
                                        fontWeight: FontWeight.bold,
                                        color: Colors.white,
                                      ),
                                      floatingLabelBehavior:
                                          FloatingLabelBehavior.always,
                                      hintStyle: TextStyle(
                                        fontSize: 14,
                                        color: Colors.black,
                                      ),
                                      contentPadding: EdgeInsets.fromLTRB(
                                          20.0, 15.0, 20.0, 15.0),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(32.0)),
                                    )),
                                    SizedBox(
                                      height: 20.0,
                                    ),
                                    TextFormField(
                                        decoration: InputDecoration(
                                      labelText: "PROFESSION",
                                      hintText: 'Student',
                                      labelStyle: TextStyle(
                                        fontSize: 18,
                                        fontWeight: FontWeight.bold,
                                        color: Colors.white,
                                      ),
                                      floatingLabelBehavior:
                                          FloatingLabelBehavior.always,
                                      hintStyle: TextStyle(
                                        fontSize: 14,
                                        color: Colors.black,
                                      ),
                                      contentPadding: EdgeInsets.fromLTRB(
                                          20.0, 15.0, 20.0, 15.0),
                                      border: OutlineInputBorder(
                                          borderRadius:
                                              BorderRadius.circular(32.0)),
                                    )),
                                    SizedBox(
                                      height: 20.0,
                                    ),
                                  ],
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                    SizedBox(
                      height: 20.0,
                    ),
                    Card(
                      margin:
                          EdgeInsets.symmetric(horizontal: 50.0, vertical: 5.0),
                      clipBehavior: Clip.antiAlias,
                      color: Color.fromRGBO(242, 248, 243, 0.5),
                      elevation: 5.0,
                      child: Padding(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 8.0, vertical: 22.0),
                        child: Row(
                          children: <Widget>[
                            Expanded(
                              child: Column(
                                children: <Widget>[
                                  SizedBox(
                                    height: 20.0,
                                  ),
                                  TextFormField(
                                      decoration: InputDecoration(
                                    labelText: "FIRST NAME",
                                    hintText: 'Nadhira',
                                    labelStyle: TextStyle(
                                      fontSize: 18,
                                      fontWeight: FontWeight.bold,
                                      color: Colors.white,
                                    ),
                                    floatingLabelBehavior:
                                        FloatingLabelBehavior.always,
                                    hintStyle: TextStyle(
                                      fontSize: 14,
                                      color: Colors.black,
                                    ),
                                    contentPadding: EdgeInsets.fromLTRB(
                                        20.0, 15.0, 20.0, 15.0),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(32.0)),
                                  )),
                                  SizedBox(
                                    height: 20.0,
                                  ),
                                  TextFormField(
                                      decoration: InputDecoration(
                                    labelText: "LAST NAME",
                                    hintText: 'Rachma',
                                    labelStyle: TextStyle(
                                      fontSize: 18,
                                      fontWeight: FontWeight.bold,
                                      color: Colors.white,
                                    ),
                                    floatingLabelBehavior:
                                        FloatingLabelBehavior.always,
                                    hintStyle: TextStyle(
                                      fontSize: 14,
                                      color: Colors.black,
                                    ),
                                    contentPadding: EdgeInsets.fromLTRB(
                                        20.0, 15.0, 20.0, 15.0),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(32.0)),
                                  )),
                                  SizedBox(
                                    height: 20.0,
                                  ),
                                  TextFormField(
                                      decoration: InputDecoration(
                                    labelText: "EMAIL",
                                    hintText: 'nadhira@gmail.com',
                                    labelStyle: TextStyle(
                                      fontSize: 18,
                                      fontWeight: FontWeight.bold,
                                      color: Colors.white,
                                    ),
                                    floatingLabelBehavior:
                                        FloatingLabelBehavior.always,
                                    hintStyle: TextStyle(
                                      fontSize: 14,
                                      color: Colors.black,
                                    ),
                                    contentPadding: EdgeInsets.fromLTRB(
                                        20.0, 15.0, 20.0, 15.0),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(32.0)),
                                  )),
                                  SizedBox(
                                    height: 20.0,
                                  ),
                                  TextFormField(
                                      decoration: InputDecoration(
                                    labelText: "MOBILE",
                                    hintText: '085714769898',
                                    labelStyle: TextStyle(
                                      fontSize: 18,
                                      fontWeight: FontWeight.bold,
                                      color: Colors.white,
                                    ),
                                    floatingLabelBehavior:
                                        FloatingLabelBehavior.always,
                                    hintStyle: TextStyle(
                                      fontSize: 14,
                                      color: Colors.black,
                                    ),
                                    contentPadding: EdgeInsets.fromLTRB(
                                        20.0, 15.0, 20.0, 15.0),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(32.0)),
                                  )),
                                  SizedBox(
                                    height: 20.0,
                                  ),
                                  TextFormField(
                                      decoration: InputDecoration(
                                    labelText: "ADDRESS",
                                    hintText: 'Jakarta, Indonesia',
                                    labelStyle: TextStyle(
                                      fontSize: 18,
                                      fontWeight: FontWeight.bold,
                                      color: Colors.white,
                                    ),
                                    floatingLabelBehavior:
                                        FloatingLabelBehavior.always,
                                    hintStyle: TextStyle(
                                      fontSize: 14,
                                      color: Colors.black,
                                    ),
                                    contentPadding: EdgeInsets.fromLTRB(
                                        20.0, 15.0, 20.0, 15.0),
                                    border: OutlineInputBorder(
                                        borderRadius:
                                            BorderRadius.circular(32.0)),
                                  )),
                                  SizedBox(
                                    height: 25.0,
                                  ),
                                  FlatButton(
                                    child: Text(
                                      'SAVE CHANGES',
                                      style: TextStyle(fontSize: 14.0),
                                    ),
                                    color: Colors.grey[800],
                                    textColor: Colors.white,
                                    onPressed: () {},
                                  ),
                                  SizedBox(
                                    height: 15.0,
                                  ),
                                  FlatButton(
                                    child: Text(
                                      'TO ACTIVITY SUMMARY',
                                      style: TextStyle(
                                        fontSize: 14.0,
                                        fontWeight: FontWeight.bold,
                                      ),
                                    ),
                                    textColor: Colors.white,
                                    onPressed: () {},
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    SizedBox(
                      height: 35.0,
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
