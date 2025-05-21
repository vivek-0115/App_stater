<template>
  <div class=" home container d-flex flex-column justify-content-center align-items-center text-center">
    <!-- Headline -->
    <h1 class="mb-3 fw-bold">Welcome to the Starter App</h1>
    
    <!-- Tagline -->
    <p class="lead mb-4">
      Kickstart your project with a clean, ready-to-use Vue + Bootstrap setup.
    </p>
    
    <!-- Buttons -->
    <div>
      <router-link to="/about" class="btn btn-primary me-3">Learn More</router-link>
      <router-link to="/signup" class="btn btn-outline-success">Get Started</router-link>
    </div>
  </div>
</template>


<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>

<style scoped>
.home{
  min-height: 90vh;
}
</style>
