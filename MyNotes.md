# inside `<script>` you can define:
## 1. Using Options API
```
<script>
export default {
  name: 'MyComponent',

  // Reactive data
  data() {
    return {
      message: 'Hello Vue!',
      count: 0
    };
  },

  // Computed properties
  computed: {
    doubleCount() {
      return this.count * 2;
    }
  },

  // Methods (event handlers, helpers, etc.)
  methods: {
    increment() {
      this.count++;
    }
  },

  // Lifecycle hooks
  created() {
    console.log('Component created');
  },
  mounted() {
    console.log('Component mounted');
  },

  // Watchers
  watch: {
    count(newVal, oldVal) {
      console.log(`Count changed from ${oldVal} to ${newVal}`);
    }
  },

  // Props
  props: {
    title: String
  },

  // Emits (if using Vue 3)
  emits: ['custom-event'],

  // Components (child components)
  components: {
    MyButton
  }
};
</script>
```

## 2. Using Composition API

```
<script setup>
import { ref, computed, watch, onMounted } from 'vue';

// Reactive variables
const count = ref(0);
const message = ref('Hello');

// Computed
const doubleCount = computed(() => count.value * 2);

// Methods
function increment() {
  count.value++;
}

// Watchers
watch(count, (newVal, oldVal) => {
  console.log(`Count changed: ${oldVal} -> ${newVal}`);
});

// Lifecycle hooks
onMounted(() => {
  console.log('Component mounted');
});
</script>
```

## 3. Vue Lifecycle Flow (Options API)
| Step | Hook                    | When It Happens                                       | What You Use It For                                                                         |
| ---- | ----------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1️⃣  | `beforeCreate`          | Right after instance is initialized                   | - Data & events **not set yet**<br>- Rarely used                                            |
| 2️⃣  | `created`               | After data & methods are set up                       | - ✅ **Good for API calls**<br>- Cannot access DOM yet                                       |
| 3️⃣  | `beforeMount`           | Just before mounting to DOM                           | - Called before the initial render                                                          |
| 4️⃣  | `mounted`               | ✅ After component is rendered into the DOM            | - ✅ **DOM is available**<br>- Use for DOM access, starting timers, API calls that affect UI |
| 5️⃣  | `beforeUpdate`          | When reactive data is about to change and re-render   | - Use to do something **before** DOM updates (like cancel timers, log changes)              |
| 6️⃣  | `updated`               | After the DOM has re-rendered due to reactive changes | - Use to do something **after** the DOM has been updated                                    |
| 7️⃣  | `beforeUnmount` (Vue 3) | Just before component is removed from the DOM         | - Cleanup (like removing listeners or clearing intervals)                                   |
| 8️⃣  | `unmounted` (Vue 3)     | After component is removed from DOM                   | - Final cleanup logic                                                                       |
## 4. Visual Summary:
App Loads →
  beforeCreate →
  created →
  beforeMount →
  mounted (✅ safe to access DOM)

Reactive data changes →
  beforeUpdate →
  updated

Component is removed →
  beforeUnmount →
  unmounted

## 5. 💡 Most commonly used:
`created()` → Fetch data early (no DOM access)

`mounted()` → Fetch data + update UI (DOM is ready)

`beforeUnmount()` → Cleanup

`unmounted()` → Final cleanup

# 🧩 Vuex Core Concepts (Quick Summary)
| Concept     | What it does                             | How it's used                        |
| ----------- | ---------------------------------------- | ------------------------------------ |
| `state`     | Stores the app's reactive data           | `this.$store.state.someValue`        |
| `getters`   | Compute derived state                    | `this.$store.getters.someGetter`     |
| `mutations` | **Synchronous** state changes            | `this.$store.commit('mutationName')` |
| `actions`   | **Asynchronous** logic (e.g., API calls) | `this.$store.dispatch('actionName')` |
