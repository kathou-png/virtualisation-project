<template>
  <div class="admin">
    <h1>This is an admin page</h1>
    <form>
        <div>
          <label for="password">Password</label>
          <input type="password" name="password" />
        </div>
        <button type="submit">Submit</button>
    </form>
    <p id="error">Username or Password is incorrect</p>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
