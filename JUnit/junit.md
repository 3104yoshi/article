### documentation
 - JUnit4 : https://github.com/junit-team/junit4/wiki
 - JUnit5 : https://junit.org/junit5/docs/current/user-guide/

### JUnit5
 - JUnit 5 = JUnit Platform + JUnit Jupiter + JUnit Vintage *1
    - JUnit Platform : It serves as a foundation of launching test framework (test engine)
    - JUnit Jupiter : It contains module specific with JUnit5, for example extention model...etc
    - JUnit Vintage : This is test engine for backward compatibility like JUnit4 or JUnit3

### diff of between JUnit4 and JUnit5
#### package
- JUnit5
 - org.junit.platform : for JUnit Platform
 - org.junit.jupiter : for Junit Jupiter
- JUnit4
 - junit.runner : for test engine
 - org.junit

#### verify an exception
 - assertThrows
#### mock functional interface

### reference
1. *1 https://junit.org/junit5/docs/current/user-guide/#overview-what-is-junit-5
2. *2 https://junit.org/junit5/docs/current/user-guide/#dependency-diagram