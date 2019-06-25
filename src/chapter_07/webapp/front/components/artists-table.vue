<template>
  <v-data-table :headers="headers" :items="artists" class="elevation-1">
    <template v-slot:items="props">
      <td>{{ props.item.name }}</td>
      <td>{{ props.item.area }}</td>
      <td>{{ props.item.aliases }}</td>
      <td>{{ props.item.begin }}</td>
      <td>{{ props.item.end }}</td>
      <td>
        <v-chip
          small
          color="green"
          text-color="white"
          v-for="tag in props.item.tags"
          v-bind:key="tag.value"
        >
          <v-avatar class="green darken-4">{{ tag.count }}</v-avatar>
          {{ tag.value }}
        </v-chip>
      </td>
      <td>
        {{ props.item.rating.value }}
        ({{ props.item.rating.count }})
      </td>
    </template>
  </v-data-table>
</template>
<script lang="ts" src="./artists-table.ts"></script>
