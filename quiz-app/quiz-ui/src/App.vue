<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <!-- <div class="wrapper"> -->
    <nav>
      <ul>
        <li>
          <RouterLink class="routers" id="admin" to="/admin"><b>ADMIN</b></RouterLink>
        </li>
        <li><img alt="Vue logo" class="logo" src="@/assets/International_Pokémon_logo.svg.png" width="120" /></li>
        <li>
          <RouterLink class="routers" id="about" to="/about"><b>ABOUT</b></RouterLink>
        </li>
        <li>
          <RouterLink class="routers" id="home" to="/"><b>HOME</b></RouterLink>
        </li>
      </ul>
    </nav>
    <!-- </div> -->

  </header>
  <RouterView />
</template>

<style>
header {
  color: darkblue;
  text-align: center;
}

header ul {
  background-color: bisque;
  border-radius: 0% 0% 50% 50%;
  box-shadow: 0 0 3px #000;
  padding: 15px;
}

header li {
  display: inline;
  text-align: center;
}

.routers {
  color: #000;
  padding: 15px;
  text-align: center;
  text-decoration: none;
  transition: .5s ease;
}

#admin {
  border-radius: 10px 100px / 120px;
  color: darkblue;
  float: left;
  margin-left: 150px;
  position: relative;
  top: -10px;
}

#admin:hover {
  color: #fff;
  background-color: green;
}

#home {
  border-radius: 10px 100px / 120px;
  color: darkblue;
  float: right;
  margin-right: 50px;
  position: relative;
  top: -10px;
}

#home:hover {
  color: #fff;
  background-color: red;
}

#about {
  border-radius: 10px 100px / 120px;
  color: darkblue;
  float: right;
  margin-right: 150px;
  position: relative;
  top: -10px;
}

#about:hover {
  color: #fff;
  background-color: cornflowerblue;
}

img {
  margin-left: 120px;
}
</style>