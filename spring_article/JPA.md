## JDBC vs JPA

- JPA provies a lot of things to developer, but it is complex
- JDBC is more simple.
- ref: https://docs.spring.io/spring-data/relational/reference/jdbc/why.html


### Repository

- JPA: just define abstract methods in repository class
- ```java
  public interface UserRepository extends JpaRepository<User, Long> {
      List<User> findByName(String name);
  }

  ```
- JDBC: define concreate methods
- ```java
  public interface UserRepository extends CrudRepository<User, Long> {
      @Query("SELECT * FROM User WHERE name = :name")
      List<User> findByName(@Param("name") String name);
  }

  ```

## HikariCP
- this is used for creating connection pool
- very fast
- default implementation in Spring Boot 
  - ref: https://docs.spring.io/spring-boot/reference/data/sql.html#data.sql.datasource.connection-pool