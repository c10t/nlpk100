<template>
  <v-data-table :headers="headers" :items="artists" class="elevation-1">
    <template v-slot:items="props">
      <td>{{ props.item.name }}</td>
      <td>{{ props.item.area }}</td>
      <td>{{ props.item.aliases }}</td>
      <td>{{ props.item.begin }}</td>
      <td>{{ props.item.end }}</td>
      <td>{{ props.item.tags }}</td>
      <td>
        {{ props.item.rating.value }}
        ({{ props.item.rating.count }})
      </td>
    </template>
  </v-data-table>
</template>
<script lang="ts" src="./artists-table.ts"></script>
