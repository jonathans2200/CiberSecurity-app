<template>
  <v-app>
    <v-container fluid>
      <v-row no-gutters class="fill-height align-center justify-center">
        <v-col cols="12" class="pa-4">
          <v-card
            class="mx-auto rounded-xl overflow-hidden"
            max-width="1280"
            elevation="12"
            :color="!scanComplete ? 'transparent' : undefined"
          >
            <v-row no-gutters>
              <v-col cols="12" md="5" class="pa-8 bg-primary-darken-1 position-relative overflow-hidden">
                <div class="position-relative" style="z-index: 2">
                  <div class="d-flex align-center mb-6">
                    <v-icon
                      icon="mdi-shield-search"
                      size="x-large"
                      color="light-blue-accent-3"
                      class="mr-3"
                    ></v-icon>
                    <h1 class="text-h3 font-weight-bold text-white">SecureScan</h1>
                  </div>

                  <p class="text-h6 text-blue-lighten-4 mb-8">
                    Plataforma completa de análisis de seguridad para detectar y neutralizar amenazas digitales.
                  </p>

                  <v-list bg-color="transparent" class="pa-0">
                    <v-list-item
                      v-for="(feature, i) in features"
                      :key="i"
                      class="px-0 py-2"
                    >
                      <template v-slot:prepend>
                        <v-avatar color="light-blue-accent-3" size="36" class="mr-3">
                          <v-icon :icon="feature.icon" color="white"></v-icon>
                        </v-avatar>
                      </template>
                      <v-list-item-title class="text-blue-lighten-4">
                        {{ feature.text }}
                      </v-list-item-title>
                    </v-list-item>
                  </v-list>
                </div>

                <div class="position-absolute circle-bg-1"></div>
                <div class="position-absolute circle-bg-2"></div>
              </v-col>

              <v-col cols="12" md="7" class="pa-8 bg-dark">
                <div v-if="scanComplete">
                  <div class="d-flex flex-column align-center py-4">
                    <v-avatar :color="threatColors[threatLevel].color" size="96" class="mb-6">
                      <v-icon :icon="threatColors[threatLevel].icon" size="x-large" color="white"></v-icon>
                    </v-avatar>

                    <h2 class="text-h4 font-weight-bold text-white mb-6">
                      {{ threatColors[threatLevel].text }}
                    </h2>

                    <v-card class="w-100 mb-6 rounded-lg" color="primary-darken-1" elevation="0">
                      <v-card-text>
                        <h3 class="text-h6 mb-4 text-white">Resultados del escaneo</h3>
                        <v-list bg-color="transparent" class="pa-0">
                          <v-list-item>
                            <v-list-item-title class="d-flex justify-space-between">
                              <span class="text-blue-lighten-3">Tipo de escaneo:</span>
                              <span class="text-white font-weight-medium">{{ tab.toUpperCase() }}</span>
                            </v-list-item-title>
                          </v-list-item>
                          <v-list-item>
                            <v-list-item-title class="d-flex justify-space-between">
                              <span class="text-blue-lighten-3">Objetivo:</span>
                              <span class="text-white font-weight-medium text-truncate" style="max-width: 200px">
                                {{ scanTarget }}
                              </span>
                            </v-list-item-title>
                          </v-list-item>
                          <v-list-item>
                            <v-list-item-title class="d-flex justify-space-between">
                              <span class="text-blue-lighten-3">Amenazas encontradas:</span>
                              <span class="text-white font-weight-medium">
                                {{ threatLevel === 0 ? '0' : threatLevel === 1 ? '2' : '7' }}
                              </span>
                            </v-list-item-title>
                          </v-list-item>
                        </v-list>
                      </v-card-text>
                    </v-card>

                    <v-btn color="primary" variant="elevated" size="large" block @click="resetScan" class="text-none rounded-lg py-3">
                      Nuevo escaneo
                    </v-btn>
                  </div>
                </div>

                <div v-else>
                  <v-tabs 
                    v-model="tab" 
                    color="primary" 
                    class="mb-8 tab-container"
                    height="56"
                  >
                    <v-tab 
                      value="file" 
                      class="custom-tab"
                      :class="{'active-tab': tab === 'file'}"
                    >
                      <v-icon icon="mdi-file-upload-outline" class="mr-2"></v-icon>
                      Archivo
                    </v-tab>
                    <v-tab 
                      value="url" 
                      class="custom-tab"
                      :class="{'active-tab': tab === 'url'}"
                      bg-color="white"
                    >
                      <v-icon icon="mdi-link-variant" class="mr-2"></v-icon>
                      URL
                    </v-tab>
                    <v-tab 
                      value="ip" 
                      class="custom-tab"
                      :class="{'active-tab': tab === 'ip'}"
                    >
                      <v-icon icon="mdi-ip-network-outline" class="mr-2"></v-icon>
                      IP
                    </v-tab>
                  </v-tabs>

                  <v-window v-model="tab" class="mb-6">
                    <v-window-item value="file">
                      <v-card
                        class="upload-card mb-6"
                        :class="{ 'upload-active': isDragging }"
                        @dragover.prevent="isDragging = true"
                        @dragleave.prevent="isDragging = false"
                        @drop.prevent="onFileDrop"
                      >
                        <v-card-text class="d-flex flex-column align-center text-center py-12">
                          <div class="upload-icon-container mb-6">
                            <v-icon 
                              icon="mdi-cloud-upload-outline" 
                              size="42" 
                              color="primary" 
                              class="upload-icon"
                            ></v-icon>
                          </div>
                          
                          <h3 class="text-h6 font-weight-medium mb-4">
                            Arrastra un archivo aquí
                          </h3>
                          
                          <p class="text-body-2 text-medium-emphasis mb-6">
                            o selecciona un archivo desde tu equipo
                          </p>
                          
                          <v-btn
                            color="primary"
                            variant="elevated"
                            prepend-icon="mdi-folder-open-outline"
                            @click="triggerFileInput"
                            class="px-6 browse-button"
                            rounded="pill"
                            size="large"
                          >
                            Buscar archivo
                          </v-btn>
                          
                          <input
                            ref="fileInput"
                            type="file"
                            @change="onFileSelected"
                            style="display: none"
                          />
                          
                          <div class="mt-6 text-caption text-medium-emphasis d-flex align-center">
                            <v-icon icon="mdi-information-outline" size="small" class="mr-1"></v-icon>
                            Tamaño máximo: 100MB
                          </div>
                        </v-card-text>
                      </v-card>
                      
                      <v-scale-transition>
                        <v-card 
                          v-if="file" 
                          class="selected-file-card mb-6"
                          color="primary"
                          variant="tonal"
                        >
                          <v-card-text class="d-flex align-center py-3">
                            <v-avatar 
                              color="primary" 
                              size="42" 
                              class="mr-3"
                            >
                              <v-icon icon="mdi-file-outline" color="white"></v-icon>
                            </v-avatar>
                            
                            <div class="flex-grow-1">
                              <div class="font-weight-medium text-truncate">
                                {{ file.name }}
                              </div>
                              <div class="text-caption">
                                {{ formatFileSize(file.size) }}
                              </div>
                            </div>
                            
                            <v-btn
                              icon="mdi-close"
                              variant="text"
                              color="primary"
                              @click="file = null"
                            ></v-btn>
                          </v-card-text>
                        </v-card>
                      </v-scale-transition>
                    </v-window-item>

                    <v-window-item value="url">
                      <v-sheet color="transparent">
                        <div class="text-body-2 font-weight-medium text-blue-lighten-3 mb-2">Introduce una URL para analizar</div>
                        <v-text-field
                          v-model="url"
                          placeholder="https://ejemplo.com"
                          variant="outlined"
                          density="comfortable"
                          bg-color="white"
                          color="primary"
                          hide-details
                          class="rounded-lg mb-2"
                          prepend-inner-icon="mdi-link"
                        ></v-text-field>
                        <div class="text-caption text-blue-lighten-4">
                          Verificaremos si contiene contenido malicioso o riesgos de seguridad
                        </div>
                      </v-sheet>
                    </v-window-item>

                    <v-window-item value="ip">
                      <v-sheet color="transparent">
                        <div class="text-body-2 font-weight-medium text-blue-lighten-3 mb-2">Introduce una dirección IP</div>
                        <v-text-field
                          v-model="ip"
                          placeholder="192.168.1.1"
                          variant="outlined"
                          density="comfortable"
                          bg-color="white"
                          color="primary"
                          hide-details
                          class="rounded-lg mb-2"
                          prepend-inner-icon="mdi-lan"
                        ></v-text-field>
                        <div class="text-caption text-blue-lighten-4">
                          Verificaremos la reputación, geolocalización y posibles amenazas
                        </div>
                      </v-sheet>
                    </v-window-item>
                  </v-window>

                  <v-btn 
                    block 
                    :color="canScan ? 'primary' : 'grey-darken-3'" 
                    :disabled="!canScan" 
                    :loading="isScanning"
                    @click="startScan"
                    size="x-large"
                    height="56"
                    class="scan-button"
                    variant="elevated"
                    outlined
                  >
                    <v-icon v-if="!isScanning" icon="mdi-magnify" class="mr-2"></v-icon>
                    <span v-if="!isScanning">Iniciar escaneo</span>
                    <template v-else>
                      <span>Escaneando</span>
                      <span class="loading-dots">...</span>
                    </template>
                  </v-btn>

                  <div class="text-center mt-4 text-caption text-medium-emphasis">
                    Al enviar aceptas los términos de uso. No subas datos personales o sensibles.
                  </div>
                </div>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    
    <!-- Sección de reporte con v-if para mostrar solo cuando hay datos -->
    <v-container v-if="dataReport" class="mt-6">
      <v-card class="rounded-xl overflow-hidden" elevation="5">
        <v-card-title class="bg-primary text-white py-4">
          <v-icon icon="mdi-file-document-outline" class="mr-2"></v-icon>
          Reporte de Análisis de Seguridad
        </v-card-title>
        <v-card-text class="pa-4">
          <MarkdownViewer :markdown="dataReport" />
        </v-card-text>
      </v-card>
    </v-container>
  </v-app>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';
import axiosInstance from '@/services/axiosInstance';  
import MarkdownViewer from '@/components/MarkdownViewer.vue';

const tab = ref('file');
const file = ref(null);
const url = ref('');
const ip = ref('');
const isScanning = ref(false);
const dataReport = ref(''); // Importante usar ref() para la variable dataReport
const scanComplete = ref(false);
const threatLevel = ref(0);
const fileInput = ref(null);
const isDragging = ref(false);

const { getAccessTokenSilently, isAuthenticated } = useAuth0();

const userRoles = ref([]);

onMounted(async () => {
  if (isAuthenticated.value) {
    try {
      const { id_token } = await getAccessTokenSilently({ detailedResponse: true });
      console.log("ID Token:", id_token); 

      // Decodificar el token para obtener los roles
      const tokenPayload = parseJwt(id_token);
      console.log("Token decodificado:", tokenPayload);

      // Extraer roles - ajusta la ruta según la estructura de tu token
      userRoles.value = tokenPayload.roles ||
                        tokenPayload['https://securityApp.com/roles'] ||
                        [];

      console.log("Roles del usuario:", userRoles.value);
    } catch (err) {
      console.error("Error al obtener el ID token:", err);
    }
  }
});

// Función para decodificar JWT sin dependencias externas
const parseJwt = (token) => {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map((c) => {
      return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
  } catch (e) {
    console.error("Error al decodificar el token:", e);
    return {};
  }
};

const features = [
  { icon: 'mdi-shield-search', text: 'Algoritmos avanzados de detección de amenazas' },
  { icon: 'mdi-clock-fast', text: 'Capacidades de escaneo en tiempo real' },
  { icon: 'mdi-earth', text: 'Red global de inteligencia de amenazas' },
];

const threatColors = [
  { color: 'success', icon: 'mdi-check-circle', text: 'No se detectaron amenazas' },
  { color: 'warning', icon: 'mdi-alert-circle', text: 'Se detectaron posibles riesgos' },
  { color: 'error', icon: 'mdi-alert', text: 'Se detectaron amenazas graves' },
];

const canScan = computed(() => {
  if (tab.value === 'file') return !!file.value;
  if (tab.value === 'url') return !!url.value;
  if (tab.value === 'ip') return !!ip.value;
  return false;
});

const scanTarget = computed(() => {
  if (tab.value === 'file') return file.value ? file.value.name : 'N/A';
  if (tab.value === 'url') return url.value || 'N/A';
  if (tab.value === 'ip') return ip.value || 'N/A';
  return 'N/A';
});

const triggerFileInput = () => fileInput.value.click();

const onFileSelected = (event) => {
  file.value = event.target.files[0] || null;
};

const onFileDrop = (event) => {
  isDragging.value = false;
  if (event.dataTransfer.files.length > 0) {
    file.value = event.dataTransfer.files[0];
  }
};

const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

const startScan = async () => {
  isScanning.value = true;
  console.log("Iniciando escaneo de tipo:", tab.value);
  
  try {
    if (tab.value === 'file' && file.value) {
      const formData = new FormData();
      formData.append('file', file.value);

      const response = await axiosInstance.post('analyze?type=file', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      // Actualizar la ref correctamente
      if (response.data && response.data.openai_response) {
        dataReport.value = response.data.openai_response;
        console.log('Markdown recibido:', dataReport.value);
      } else {
        console.error('No se recibió respuesta de análisis');
      }
    }

    // Simulación de escaneo y actualización de estado
    setTimeout(() => {
      isScanning.value = false;
      scanComplete.value = true;
      threatLevel.value = Math.floor(Math.random() * 3);
    }, 2000);
  } catch (error) {
    console.error('Error durante el análisis:', error);
    isScanning.value = false;
    // Opcional: Mostrar mensaje de error al usuario
  }
};

const resetScan = () => {
  scanComplete.value = false;
  threatLevel.value = 0;
  dataReport.value = ''; // Limpiar el reporte al reiniciar
  if (tab.value === 'file') file.value = null;
  else if (tab.value === 'url') url.value = '';
  else if (tab.value === 'ip') ip.value = '';
};
</script>

<style>
.bg-gradient {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
}

.bg-dark {
  background-color: #101828 !important;
}

.circle-bg-1 {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(33, 150, 243, 0.1) 0%, rgba(33, 150, 243, 0) 70%);
  top: -100px;
  right: -50px;
  z-index: 1;
}

.circle-bg-2 {
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(3, 169, 244, 0.1) 0%, rgba(3, 169, 244, 0) 70%);
  bottom: -50px;
  left: -50px;
  z-index: 1;
}

.tab-container {
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  overflow: hidden;
}

.custom-tab {
  min-width: 120px;
  border-radius: 16px !important;
  text-transform: none !important;
  font-weight: 500 !important;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
  color: white !important;
}

.active-tab {
  background-color: rgba(33, 150, 243, 0.15);
}

.upload-card {
  border: 2px dashed rgba(33, 150, 243, 0.3);
  border-radius: 16px;
  background-color: rgba(33, 150, 243, 0.05);
  transition: all 0.3s ease;
}

.upload-card:hover, .upload-active {
  border-color: #2196F3;
  background-color: rgba(33, 150, 243, 0.1);
}

.upload-icon-container {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(33, 150, 243, 0.1);
}

.upload-icon {
  animation: float 3s ease-in-out infinite;
}

.browse-button {
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
  transition: all 0.3s ease;
}

.browse-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 14px rgba(33, 150, 243, 0.4);
}

.selected-file-card {
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.scan-button {
  border-radius: 12px;
  font-weight: 500;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.3);
  transition: all 0.3s ease;
}

.scan-button:not(:disabled):hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 14px rgba(33, 150, 243, 0.4);
}

.loading-dots {
  display: inline-block;
  width: 24px;
  text-align: left;
  animation: ellipsis 1.5s infinite;
}

@keyframes float {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
  100% {
    transform: translateY(0px);
  }
}

@keyframes ellipsis {
  0% {
    content: ".";
  }
  33% {
    content: "..";
  }
  66% {
    content: "...";
  }
}
</style>