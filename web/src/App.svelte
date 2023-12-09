<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
</script>

<main>
  <div id="homePanel">
    <div id="createRoomBox" class="roomBox">
      <h1>Create new room</h1>
      <input type="text" placeholder="ID">
      <button type="submit">Create</button>
    </div>
    <div id="joinRoomBox" class="roomBox">
      <h1>Join room</h1>
      <input type="text" placeholder="ID">
      <button type="submit">Join</button>
    </div>
  </div>
</main>

<style>
#homePanel{
  display: flex;
  justify-content: center;
  align-items: center;
}
.roomBox{
  text-align: center;
  margin: 5%;
}
</style>
