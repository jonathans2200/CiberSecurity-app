<template>
  <div>
    <hero />
    <hr />
  </div>
</template>

<script lang="ts">
import Hero from "../components/Hero.vue";

export default {
  name: "home-view",
  components: {
    Hero,
  },
};
</script>

<style lang="css" scoped>
.next-steps .fa-link {
    margin-right: 5px;
}
</style>
