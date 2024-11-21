### documentation

- JUnit4 : https://github.com/junit-team/junit4/wiki
- JUnit5 : https://junit.org/junit5/docs/current/user-guide/

### JUnit5

- JUnit 5 = JUnit Platform + JUnit Jupiter + JUnit Vintage *1
  - JUnit Platform : It serves as a foundation of launching test framework (test engine)
  - JUnit Jupiter : It contains module specific with JUnit5, for example extention model...etc
  - JUnit Vintage : This is test engine for backward compatibility like JUnit4 or JUnit3JUnit4

### JUnit4
- Runner : JUnit4 is recommended (@Runwith(JUni4.class))
  - BlockJUnit4ClassRunner is current version's default runner
  - but JUnit4 will always invoke latest default runner

### diff of between JUnit4 and JUnit5

#### package

- JUnit5
- org.junit.platform : for JUnit Platform
- org.junit.jupiter : for Junit Jupiter
- JUnit4
- junit.runner : for test engine
- org.junit

#### verify an exception

- assertThrows (added in JUnit 4.13)

#### verify functional interface created in method

- To test SampleApplication#test
  - to confirm that sampleFunctional#executeSampleFunction receives functional if expected.
  - This functional IF doesn't have equals and hashcode method, and also isn't injected as argument.
  - So, simply applying Mockito.when doesn't work.
  - We can test it with thenAnswer(), which can fetch method's argument that is actually passed. 

```java
@Component
public class SampleApplication {

    private final SampleFunctionalIFExecutor sampleFunctionalIFExecutor;

    public SampleApplicationRunner(SampleFunctionalIFExecutor sampleFunctionalIFExecutor) {
        this.sampleFunctionalIFExecutor = sampleFunctionalIFExecutor;
    }

    public String test(String key) {
        SampleFunctionalIF sampleFunctionalIF = () -> key;
        return sampleFunctionalIFExecutor.executeSampleFunction(sampleFunctionalIF);
    }
}

@FunctionalInterface
@Component
public interface SampleFunctionalIF {
    String execute();
}

@Component
public class SampleFunctionalIFExecutor {

    public String executeSampleFunction(SampleFunctionalIF sampleFunctionalIF) {
        return sampleFunctionalIF.execute();
    }
}
```

- test code

```java
    @Test
    void testMethod() {
        when(sampleFunctionalIfExecutor.executeSampleFunction(any(SampleFunctionalIF.class))).thenAnswer(invocation -> {
            SampleFunctionalIF sampleFunctionalIF = invocation.getArgument(0);
            assertEquals("Hello World", sampleFunctionalIF.execute());
            return "Hello World";
        });
        runner.test("Hello World");
    }
```

### reference

1. *1 https://junit.org/junit5/docs/current/user-guide/#overview-what-is-junit-5
2. *2 https://junit.org/junit5/docs/current/user-guide/#dependency-diagram
