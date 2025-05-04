<template>
  <v-container>
    <v-card class="rounded-xl elevation-3 overflow-hidden">
      <v-row no-gutters>
        <!-- Sidebar con información principal -->
        <v-col cols="12" md="4" class="bg-primary">
          <v-card-item class="d-flex flex-column align-center py-8">
            <v-avatar size="120" class="mb-4 elevation-4 border-avatar">
              <v-img
                :src="user?.picture"
                :alt="`${user?.name}'s profile picture`"
                cover
              />
            </v-avatar>
            <h2 class="text-h4 font-weight-bold text-white mb-1">{{ user?.name }}</h2>
            <p class="text-subtitle-1 text-blue-lighten-4">{{ user?.nickname }}</p>
            
            <!-- Sección de roles mejorada -->
            <div class="roles-section mt-6 px-4 w-100">
              <h3 class="text-h6 text-white mb-3 d-flex align-center">
                <v-icon icon="mdi-shield-account" class="mr-2" color="blue-lighten-4"></v-icon>
                Roles de Usuario
              </h3>
              <v-card flat class="bg-blue-lighten-5 rounded-lg pa-2">
                <div v-if="userRoles.length > 0">
                  <v-list-item
                    v-for="(role, index) in userRoles"
                    :key="index"
                    density="compact"
                    class="rounded px-2 mb-1"
                    :class="getRoleColorClass(role)"
                  >
                    <template v-slot:prepend>
                      <v-icon :icon="getRoleIcon(role)" size="small" color="white"></v-icon>
                    </template>
                    <v-list-item-title class="font-weight-medium text-white">
                      {{ formatRoleName(role) }}
                    </v-list-item-title>
                  </v-list-item>
                </div>
                <div v-else class="text-center py-2 text-subtitle-2 text-primary-darken-1">
                  Sin roles asignados
                </div>
              </v-card>
            </div>
          </v-card-item>
        </v-col>

        <!-- Contenido principal -->
        <v-col cols="12" md="8">
          <v-card-text class="pa-6">
            <!-- Información del usuario -->
            <h3 class="text-h5 font-weight-bold mb-4">Información de Usuario</h3>
            
            <v-list lines="two">
              <v-list-item>
                <template v-slot:prepend>
                  <v-avatar color="primary" size="36" class="mr-4">
                    <v-icon icon="mdi-email" color="white"></v-icon>
                  </v-avatar>
                </template>
                <v-list-item-title class="font-weight-medium">Correo electrónico</v-list-item-title>
                <v-list-item-subtitle>
                  <span>{{ user?.email }}</span>
                  <v-chip
                    v-if="user?.email_verified"
                    size="x-small"
                    color="success"
                    variant="flat"
                    class="ml-2"
                  >
                    Verificado
                  </v-chip>
                </v-list-item-subtitle>
              </v-list-item>
              
              <v-list-item>
                <template v-slot:prepend>
                  <v-avatar color="primary" size="36" class="mr-4">
                    <v-icon icon="mdi-account" color="white"></v-icon>
                  </v-avatar>
                </template>
                <v-list-item-title class="font-weight-medium">Usuario</v-list-item-title>
                <v-list-item-subtitle>{{ user?.nickname }}</v-list-item-subtitle>
              </v-list-item>
              
              <v-list-item>
                <template v-slot:prepend>
                  <v-avatar color="primary" size="36" class="mr-4">
                    <v-icon icon="mdi-update" color="white"></v-icon>
                  </v-avatar>
                </template>
                <v-list-item-title class="font-weight-medium">Última actualización</v-list-item-title>
                <v-list-item-subtitle>{{ formatDate(user?.updated_at) }}</v-list-item-subtitle>
              </v-list-item>
              
              <v-list-item>
                <template v-slot:prepend>
                  <v-avatar color="primary" size="36" class="mr-4">
                    <v-icon icon="mdi-identifier" color="white"></v-icon>
                  </v-avatar>
                </template>
                <v-list-item-title class="font-weight-medium">ID de usuario</v-list-item-title>
                <v-list-item-subtitle class="text-truncate">{{ user?.sub }}</v-list-item-subtitle>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
import { computed } from 'vue';

const { user } = useAuth0();

const userRoles = computed(() => {
  if (user.value && user.value['https://securityApp.com/roles']) {
    return user.value['https://securityApp.com/roles'];
  }
  return [];
});

const formatDate = (dateString) => {
  if (!dateString) return '';
  
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('es-ES', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  }).format(date);
};

const formatRoleName = (role) => {
  if (!role) return '';
  return role
    .replace(/([A-Z])/g, ' $1')
    .replace(/^./, (str) => str.toUpperCase())
    .trim();
};

const getRoleIcon = (role) => {
  const roleToLower = role.toLowerCase();
  
  if (roleToLower.includes('admin')) return 'mdi-shield-crown';
  if (roleToLower.includes('security')) return 'mdi-shield-lock';
  if (roleToLower.includes('manager')) return 'mdi-account-cog';
  if (roleToLower.includes('dev') || roleToLower.includes('developer')) return 'mdi-code-braces';
  if (roleToLower.includes('analyst')) return 'mdi-chart-line';
  if (roleToLower.includes('user')) return 'mdi-account';
  
  return 'mdi-shield-account';
};

const getRoleColorClass = (role) => {
  const roleToLower = role.toLowerCase();
  
  if (roleToLower.includes('admin')) return 'bg-red-darken-1';
  if (roleToLower.includes('security')) return 'bg-purple-darken-1';
  if (roleToLower.includes('manager')) return 'bg-indigo-darken-1';
  if (roleToLower.includes('dev') || roleToLower.includes('developer')) return 'bg-deep-purple-darken-1';
  if (roleToLower.includes('analyst')) return 'bg-blue-darken-1';
  if (roleToLower.includes('user')) return 'bg-teal-darken-1';
  
  return 'bg-blue-darken-2';
};

const formattedJson = computed(() => {
  return JSON.stringify(user.value, null, 2);
});
</script>

<style scoped>
.border-avatar {
  border: 3px solid rgba(255, 255, 255, 0.8);
}

.code-block {
  overflow-x: auto;
  font-family: monospace;
  font-size: 14px;
}

.roles-section {
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  padding-top: 1.5rem;
}
</style>