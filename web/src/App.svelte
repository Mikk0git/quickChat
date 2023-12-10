<script lang="ts">

const serverURL:string = "http://127.0.0.1:5000"

let roomId: string
let roomPassword: string
let username: string

function createRoom() {
  console.log("Creating room id: "+ roomId)

  fetch(serverURL+"/create-room", {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
	    "id": roomId,
	    "password": roomPassword,
      "username" : username,
    })
  })

}


function joinRoom() {
  console.log("Joining room id: "+ roomId)

}

</script>

<main>
  <div id="homePanel">
    <input type="text" placeholder="username" bind:value={username}>
    <div id="createRoomBox" class="roomBox">
      <h1>Create new room</h1>
      <input type="text" placeholder="ID" bind:value={roomId}>
      <input type="text" placeholder="Password" bind:value={roomPassword}>
      <button type="submit" on:click={createRoom}>Create</button>
    </div>
    <div id="joinRoomBox" class="roomBox">
      <h1>Join room</h1>
      <input type="text" placeholder="ID" bind:value={roomId}>
      <button type="submit" on:click={joinRoom}>Join</button>
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
