<template>
  <nav class="navbar navbar-expand-md navbar-light shadow-sm">
    <div class="container">
      <!-- Brand -->
      <a class="navbar-brand d-flex align-items-center" href="#">
        <div class="bg-primary rounded-circle d-flex align-items-center justify-content-center"
          style="width: 32px; height: 32px;">
          <span class="text-white fw-bold">L</span>
        </div>
        <span class="ms-2 fw-semibold">Brand Name</span>
      </a>

      <!-- Toggler -->
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon text-primary"></span>
      </button>

      <!-- Links -->
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <!-- Admin Links -->
        <ul v-if="isAuthenticated && userRole === 'Admin'" class="navbar-nav ms-auto mb-2 mb-md-0">
          <div class="navbar-nav me-4">
            <router-link :to="`/admin/${this.userId}/dashboard`" class="nav-link">Dashboard</router-link>
            <router-link :to="`/admin/${this.userId}/users`" class="nav-link">Users</router-link>
            <router-link :to="`/admin/${this.userId}/profile`" class="nav-link">Profile</router-link>
            <span @click="handleLogout()" class="nav-link fw-bold" style="cursor: pointer;"> Logout </span>
          </div>

          <div class="d-flex ms-4">
            <div id="profile-img" class="bg-secondary">
              <img src="" alt=" ">
            </div>
            <div v-if="userData" class="d-flex ms-2 text-decoration-underline align-items-center">
              {{ userData.first_name }} {{ userData.last_name }}
            </div>
          </div>
        </ul>

        <!-- User Links -->
        <ul v-else-if="isAuthenticated && userRole === 'User'" class="navbar-nav ms-auto mb-2 mb-md-0">
          <div class="navbar-nav me-4">
            <router-link :to="`/user/${this.userId}/dashboard`" class="nav-link">Dashboard</router-link>
            <router-link :to="`/user/${this.userId}/profile`" class="nav-link">Profile</router-link>
            <span @click="handleLogout()" class="nav-link fw-bold" style="cursor: pointer;"> Logout </span>
          </div>

          <div class="d-flex ms-4">
            <div id="profile-img" class="bg-secondary">
              <img src="" alt=" ">
            </div>
            <div v-if="userData" class="d-flex ms-2 text-decoration-underline align-items-center">
              {{ userData.first_name }} {{ userData.last_name }}
            </div>
          </div>
        </ul>

        <ul v-else class="navbar-nav ms-auto mb-2 mb-md-0">
          <router-link to="/" class="nav-link">Home</router-link>
          <router-link to="/about" class="nav-link">About</router-link>
          <router-link to="/signup" class="nav-link">SignUp</router-link>
          <router-link to="/login" class="nav-link">LogIn</router-link>
        </ul>

      </div>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex';
import { mapGetters } from 'vuex';

const stored = sessionStorage.getItem('authData');
const authData = stored ? JSON.parse(stored) : {};

export default {
  name: 'NavBar',

computed: {
  ...mapState(['authData', 'isAuthenticated']),
  ...mapGetters(['userData']),
  userRole() {
    return this.authData?.role;
  },
  userId() {
    return this.authData?.id;
  }
},
  methods: {
    async handleLogout() {
      this.$router.push({ name: 'login' });
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style scoped>
#profile-img,
#profile-img img {
  height: 2.5rem;
  width: 2.5rem;
  border-radius: 50%;
}
</style>