<template>
  <GmapMap
    :center="center"
    :zoom="13"
    style="height: 1000px; width: 2000px;"
    >
    <GmapMarker
      :key="index"
      v-for="(m, index) in markers"
      :position="m.position"
      :clickable="true"
      :draggable="true"
      @click="center=m.position"
      />
  </GmapMap>
</template>

<script>
export default {
  data () {
    return {
      center: { lat: 41.83, lng: -87.623 },
      markers: [
        {
          position: { lat: 41.788, lng: -87.5987 }
        },
        {
          position: { lat: 41.8676, lng: -87.614 }
        }
      ]
    }
  }
}
</script>
