<template>
  <v-data-table :headers="headers" :items="artists" class="elevation-1">
    <template v-slot:items="props">
      <td>{{ props.item.name }}</td>
    </template>
  </v-data-table>
</template>
<script lang="ts" src="./artists-table.ts"></script>
