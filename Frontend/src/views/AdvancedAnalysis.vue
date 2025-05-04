<template>
  <v-app>
    <v-container fluid>
      <v-row no-gutters class="fill-height align-center justify-center">
        <v-col cols="12" class="pa-4">
          <v-card
            class="mx-auto rounded-xl overflow-hidden"
            max-width="1000"
            elevation="12"
            :color="!scanComplete ? 'transparent' : undefined"
          >
            <v-row no-gutters>
              <v-col cols="12" md="5" class="pa-8 bg-primary-darken-1 position-relative overflow-hidden">
                <div class="position-relative" style="z-index: 2">
                  <div class="d-flex align-center mb-6">
                    <v-icon
                      icon="mdi-link-lock"
                      size="x-large"
                      color="light-blue-accent-3"
                      class="mr-3"
                    ></v-icon>
                    <h1 class="text-h3 font-weight-bold text-white">URLShield</h1>
                  </div>

                  <p class="text-h6 text-blue-lighten-4 mb-8">
                    Análisis de seguridad avanzado para detectar URLs maliciosas y proteger tu navegación.
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
                  
                  <div class="mt-8 pt-4">
                    <div class="text-caption text-blue-lighten-5 mb-2">Powered by</div>
                    <div class="d-flex align-center">
                      <v-icon icon="mdi-shield-check" size="small" color="light-blue-accent-3" class="mr-2"></v-icon>
                      <span class="text-body-2 text-blue-lighten-5">ThreatIntel Global Network</span>
                    </div>
                  </div>
                </div>

                <div class="position-absolute circle-bg-1"></div>
                <div class="position-absolute circle-bg-2"></div>
              </v-col>

              <v-col cols="12" md="7" class="pa-8 bg-dark">
                <div v-if="scanComplete">
                  <div class="d-flex flex-column align-center py-4">
                    <v-avatar color="primary" size="96" class="mb-6">
                      <v-icon icon="mdi-check-circle" size="x-large" color="white"></v-icon>
                    </v-avatar>

                    <h2 class="text-h4 font-weight-bold text-white mb-6">
                      Análisis Completado
                    </h2>

                    <v-card class="w-100 mb-6 rounded-lg" color="primary-darken-1" elevation="0">
                      <v-card-text>
                        <h3 class="text-h6 mb-4 text-white">Resultados del escaneo</h3>
                        <v-list bg-color="transparent" class="pa-0">
                          <v-list-item>
                            <v-list-item-title class="d-flex justify-space-between">
                              <span class="text-blue-lighten-3">URL analizada:</span>
                              <span class="text-white font-weight-medium text-truncate" style="max-width: 250px">
                                {{ url }}
                              </span>
                            </v-list-item-title>
                          </v-list-item>
                          <v-list-item>
                            <v-list-item-title class="d-flex justify-space-between">
                              <span class="text-blue-lighten-3">Fecha del análisis:</span>
                              <span class="text-white font-weight-medium">
                                {{ new Date().toLocaleString() }}
                              </span>
                            </v-list-item-title>
                          </v-list-item>
                        </v-list>
                      </v-card-text>
                    </v-card>

                    <v-btn color="primary" variant="elevated" size="large" block @click="resetScan" class="text-none rounded-lg py-3">
                      <v-icon icon="mdi-refresh" class="mr-2"></v-icon>
                      Escanear otra URL
                    </v-btn>

                     <v-btn 
                      v-if="pdfBase64"
                      color="accent" 
                      variant="elevated" 
                      size="large" 
                      block 
                      @click="downloadPdf" 
                      class="text-none rounded-lg py-3 mt-4"
                    >
                      <v-icon icon="mdi-file-pdf-box" class="mr-2"></v-icon>
                      Descargar Informe PDF
                    </v-btn>
                  </div>

                </div>
                
                <!-- Scan Input Section -->
                <div v-else>
                  <div class="text-h5 font-weight-bold text-white mb-6">
                    Escaneo de URL
                  </div>
                  
                  <v-card class="mb-8 rounded-lg pa-6" color="primary-darken-2" elevation="0">
                    <div class="d-flex align-center mb-4">
                      <v-avatar color="light-blue-accent-3" size="36" class="mr-3">
                        <v-icon icon="mdi-shield-search" color="white"></v-icon>
                      </v-avatar>
                      <span class="text-h6 text-white">Comprueba si una URL es segura</span>
                    </div>
                    
                    <p class="text-blue-lighten-4 mb-4">
                      Nuestro sistema analiza las URLs en busca de malware, phishing, contenido malicioso y otras 
                      amenazas de seguridad antes de que las visites.
                    </p>
                  </v-card>

                  <div class="text-body-1 font-weight-medium text-blue-lighten-3 mb-3">Introduce la URL que deseas analizar</div>
                  <v-text-field
                    v-model="url"
                    placeholder="https://ejemplo.com"
                    variant="outlined"
                    density="comfortable"
                    bg-color="white"
                    color="primary"
                    class="rounded-lg mb-2"
                    :error-messages="urlError ? [urlError] : []"
                    @input="validateUrl"
                    @keyup.enter="startScan"
                    autocomplete="off"
                    :disabled="isScanning"
                    hide-details="auto"
                    prepend-inner-icon="mdi-link"
                  ></v-text-field>
                  
                  <div class="text-caption text-blue-lighten-4 mb-6">
                    URLShield verificará si contiene contenido malicioso o riesgos de seguridad
                  </div>

                  <v-btn 
                    block 
                    :color="canScan ? 'primary' : 'grey-darken-3'" 
                    :disabled="!canScan" 
                    :loading="isScanning"
                    @click="startScan"
                    size="x-large"
                    height="56"
                    class="scan-button mb-4"
                    variant="elevated"
                  >
                    <v-icon v-if="!isScanning" icon="mdi-link-check" class="mr-2"></v-icon>
                    <span v-if="!isScanning">Analizar URL</span>
                    <template v-else>
                      <span>Analizando</span>
                      <span class="loading-dots">...</span>
                    </template>
                  </v-btn>
                  
                  <v-sheet class="scan-features" color="transparent" rounded>
                    <v-row>
                      <v-col cols="6" v-for="(item, i) in scanFeatures" :key="i">
                        <div class="d-flex align-center py-1">
                          <v-icon icon="mdi-check-circle" color="primary" size="small" class="mr-2"></v-icon>
                          <span class="text-caption text-blue-lighten-3">{{ item }}</span>
                        </div>
                      </v-col>
                    </v-row>
                  </v-sheet>

                  <div class="text-center mt-6 text-caption text-medium-emphasis">
                    Al enviar aceptas los términos de uso. No compartimos tus URLs con terceros.
                  </div>
                </div>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
      <v-card v-if="dataReport" class="mt-6 rounded-xl overflow-hidden" elevation="5">
        <v-card-title class="bg-primary text-white py-4">
          <v-icon icon="mdi-text-box-search-outline" class="mr-2"></v-icon>
          Reporte Detallado del Análisis
        </v-card-title>
        <v-card-text class="pa-4">
          <MarkdownViewer :markdown="dataReport" />
        </v-card-text>
    </v-card>
  </v-app>
</template>

<script setup>
import axiosInstance from '@/services/axiosInstance';
import { ref, computed } from 'vue';
import MarkdownViewer from '@/components/MarkdownViewer.vue';

const url = ref('');
const urlError = ref('');
const isScanning = ref(false);
const scanComplete = ref(false);
const dataReport = ref('');
const pdfBase64 = ref('');
const errorMessage = ref('');

const features = [
  { icon: 'mdi-web-check', text: 'Detección avanzada de phishing y estafas' },
  { icon: 'mdi-bug-check', text: 'Análisis de malware y códigos maliciosos' },
  { icon: 'mdi-shield-lock', text: 'Verificación de certificados SSL y seguridad' },
  { icon: 'mdi-database-check', text: 'Base de datos global de URLs peligrosas' },
];

const scanFeatures = [
  'Análisis de malware',
  'Detección de phishing',
  'Verificación SSL',
  'Redireccionamientos',
  'Seguridad DNS',
  'Reputación del dominio',
];

const canScan = computed(() => {
  return url.value && !urlError.value && !isScanning.value;
});

const validateUrl = () => {
  if (!url.value) {
    urlError.value = '';
    return;
  }
  
  // Patrón básico para validar URLs
  const pattern = /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w.-]*)*\/?$/;
  
  // Si no comienza con http o https, añadimos https://
  if (!/^https?:\/\//i.test(url.value)) {
    url.value = 'https://' + url.value;
  }
  
  if (!pattern.test(url.value)) {
    urlError.value = 'URL inválida. Formato: https://ejemplo.com';
  } else {
    urlError.value = '';
  }
};

const startScan = async () => {
  if (!canScan.value) return;

  isScanning.value = true;
  urlError.value = '';
  errorMessage.value = '';
  dataReport.value = '';
  pdfBase64.value = '';
  scanComplete.value = false;

  try {
    validateUrl();
    if (urlError.value) {
      throw new Error('URL inválida.');
    }

    const payload = {
      type: 'url',
      value: url.value.trim()
    };
    
    const response = await axiosInstance.post('/advanced-analysis', payload);
    
    if (response.data) {
      if (response.data.openai_response) {
        dataReport.value = response.data.openai_response;
      } else if (response.data.report) {
        dataReport.value = response.data.report;
      }
      
      if (response.data.pdf_base64) {
        pdfBase64.value = response.data.pdf_base64;
      }
      
      scanComplete.value = true;
    } else {
      throw new Error('Respuesta de análisis inválida o vacía.');
    }
  } catch (error) {
    console.error('Error en el escaneo:', error);
    
    if (error.response) {
      errorMessage.value = `Error del servidor: ${error.response.status} - ${error.response.data?.detail || 'Error desconocido'}`;
    } else if (error.request) {
      errorMessage.value = 'No se pudo conectar con el servidor. Verifica tu conexión o inténtalo más tarde.';
    } else {
      errorMessage.value = `Error: ${error.message}`;
    }
    
    scanComplete.value = false;
  } finally {
    isScanning.value = false;
  }
};

const downloadPdf = () => {
  if (!pdfBase64.value) return;
  try {
    const byteCharacters = atob(pdfBase64.value);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
      byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);

    const blob = new Blob([byteArray], { type: 'application/pdf' });

    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'advanced_report.pdf';

    document.body.appendChild(link);
    link.click();

    document.body.removeChild(link);
    URL.revokeObjectURL(link.href);
  } catch (error) {
    console.error("Error al descargar PDF:", error);
  }
};

const resetScan = () => {
  url.value = '';
  urlError.value = ''; 
  dataReport.value = '';
  pdfBase64.value = ''; 
  scanComplete.value = false;
  errorMessage.value = '';
  isScanning.value = false;
};
</script>

<style>
.bg-primary {
  background-color: #1976D2 !important;
}

.bg-gradient {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
}

.bg-dark {
  background-color: #101828 !important;
}

.bg-primary-darken-1 {
  background-color: #0D47A1 !important;
}

.bg-primary-darken-2 {
  background-color: rgba(13, 71, 161, 0.2) !important;
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

.scan-features {
  background-color: rgba(33, 150, 243, 0.05);
  border: 1px solid rgba(33, 150, 243, 0.1);
  border-radius: 12px;
  padding: 12px;
}

.loading-dots {
  display: inline-block;
  width: 24px;
  text-align: left;
  animation: ellipsis 1.5s infinite;
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