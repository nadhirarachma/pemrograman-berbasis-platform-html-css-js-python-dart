import 'package:flutter/material.dart';
import 'package:lab_7/screens/summary.dart';
import '../widgets/main_drawer.dart';

class EditProfileApp extends StatelessWidget {
  const EditProfileApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Edit Profile',
      theme: ThemeData(
          appBarTheme: AppBarTheme(
        color: const Color(0xFF000000),
      )),
      home: EditForm(),
    );
  }
}

class EditForm extends StatefulWidget {
  const EditForm({Key? key}) : super(key: key);

  @override
  EditApp createState() {
    return EditApp();
  }
}

class EditApp extends State<EditForm> {
  final _formKey = GlobalKey<FormState>();
  String username = "";
  String gender = "";
  String age = "";
  String profession = "";
  String firstname = "";
  String lastname = "";
  String email = "";
  String mobile = "";
  String address = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("e-Nadi", style: TextStyle(color: Colors.red)),
        backgroundColor: Colors.black,
      ),
      drawer: MainDrawer(),
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
                    Form(
                      key: _formKey,
                      child: Column(children: <Widget>[
                        Card(
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
                                    crossAxisAlignment:
                                        CrossAxisAlignment.center,
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
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            username = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      TextFormField(
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            gender = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      TextFormField(
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            age = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      TextFormField(
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            profession = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                        SizedBox(
                          height: 20.0,
                        ),
                        Card(
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
                                    children: <Widget>[
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      TextFormField(
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            firstname = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      TextFormField(
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            lastname = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      TextFormField(
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            email = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      TextFormField(
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            mobile = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                      SizedBox(
                                        height: 20.0,
                                      ),
                                      TextFormField(
                                          validator: (value) {
                                            if (value == null ||
                                                value.isEmpty) {
                                              return 'Please fill out this field.';
                                            }
                                            address = value;
                                            return null;
                                          },
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
                                                    BorderRadius.circular(
                                                        32.0)),
                                          )),
                                      SizedBox(
                                        height: 25.0,
                                      ),
                                      Padding(
                                        padding: const EdgeInsets.symmetric(
                                            vertical: 16.0),
                                        child: ElevatedButton(
                                          style: ButtonStyle(
                                            backgroundColor:
                                                MaterialStateProperty.all(
                                                    Colors.grey[800]),
                                          ),
                                          onPressed: () {
                                            if (_formKey.currentState!
                                                .validate()) {
                                              print(username);
                                              print(gender);
                                              print(age);
                                              print(profession);
                                              print(firstname);
                                              print(lastname);
                                              print(email);
                                              print(mobile);
                                              print(address);

                                              showDialog(
                                                context: context,
                                                builder: (context) {
                                                  return AlertDialog(
                                                    content: Text(
                                                        'Profile Successfully Updated!'),
                                                    actions: <Widget>[
                                                      TextButton(
                                                          child: Text('Ok'),
                                                          onPressed: () {
                                                            Navigator.push(
                                                                context,
                                                                MaterialPageRoute(
                                                                    builder:
                                                                        (context) =>
                                                                            ActivitySummaryApp()));
                                                          }),
                                                    ],
                                                  );
                                                },
                                              );
                                            }
                                          },
                                          child: const Text('SAVE CHANGES'),
                                        ),
                                      ),
                                      TextButton(
                                        child: Text(
                                          'TO ACTIVITY SUMMARY',
                                          style: TextStyle(
                                            fontSize: 14.0,
                                            fontWeight: FontWeight.bold,
                                            color: Colors.white,
                                          ),
                                        ),
                                        onPressed: () {
                                          Navigator.push(
                                              context,
                                              MaterialPageRoute(
                                                  builder: (context) =>
                                                      ActivitySummaryApp()));
                                        },
                                      ),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ]),
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
