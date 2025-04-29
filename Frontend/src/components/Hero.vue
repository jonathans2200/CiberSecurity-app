<template>
  <v-app>


    <v-main class="bg-grey-lighten-4">
      <!-- Hero Section -->
      <v-container fluid class="pa-0">
        <v-row no-gutters>
          <v-col cols="12">
            <v-sheet
              class="bg-deep-purple"
              height="500"
            >
              <v-container class="fill-height">
                <v-row align="center">
                  <v-col cols="12" md="6" class="text-white">
                    <h1 class="text-h2 font-weight-bold mb-4">Detección inteligente de amenazas</h1>
                    <p class="text-h6 mb-8">
                      Analiza archivos, URLs e IPs en segundos y recibe recomendaciones de seguridad personalizadas.
                    </p>
                    <div class="d-flex flex-wrap gap-4">
                      <v-btn
                        size="large"
                        color="white"
                        variant="elevated"
                        class="text-deep-purple"
                      >
                        <v-icon start>mdi-rocket-launch</v-icon>
                        Comenzar ahora
                      </v-btn>
                      <v-btn
                        size="large"
                        color="deep-purple-lighten-4"
                        variant="tonal"
                      >
                        <v-icon start>mdi-play-circle</v-icon>
                        Ver demostración
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="12" md="6" class="d-flex justify-center align-center">
                    <v-img
                      src="/api/placeholder/600/400"
                      alt="Security Analysis Dashboard"
                      class="rounded-lg"
                      max-width="500"
                    ></v-img>
                  </v-col>
                </v-row>
              </v-container>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>

      <!-- Features Section -->
      <v-container class="py-12">
        <v-row class="mb-6">
          <v-col cols="12" class="text-center">
            <h2 class="text-h3 font-weight-bold mb-2">Características principales</h2>
            <p class="text-subtitle-1">Descubre cómo nuestra plataforma te mantiene seguro</p>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="4">
            <v-card height="100%" class="pa-4" variant="outlined">
              <v-icon icon="mdi-file-search-outline" size="42" color="deep-purple" class="mb-4"></v-icon>
              <v-card-title class="text-h5 pa-0">Análisis de archivos</v-card-title>
              <v-card-text class="pa-0 pt-2">
                <p>Detecta malware, virus, ransomware y otras amenazas en tus archivos antes de abrirlos. Compatible con múltiples formatos.</p>
                <v-list density="compact" class="bg-transparent pa-0 mt-2">
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Escaneo de virus y malware</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Detección de código malicioso</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Verificación de firma digital</div>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" md="4">
            <v-card height="100%" class="pa-4" variant="outlined">
              <v-icon icon="mdi-web-check" size="42" color="deep-purple" class="mb-4"></v-icon>
              <v-card-title class="text-h5 pa-0">Análisis de URLs</v-card-title>
              <v-card-text class="pa-0 pt-2">
                <p>Verifica la seguridad de enlaces y sitios web antes de visitarlos para protegerte contra phishing y sitios maliciosos.</p>
                <v-list density="compact" class="bg-transparent pa-0 mt-2">
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Detección de phishing</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Verificación de certificados SSL</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Evaluación de contenido malicioso</div>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" md="4">
            <v-card height="100%" class="pa-4" variant="outlined">
              <v-icon icon="mdi-ip-network-outline" size="42" color="deep-purple" class="mb-4"></v-icon>
              <v-card-title class="text-h5 pa-0">Análisis de IPs</v-card-title>
              <v-card-text class="pa-0 pt-2">
                <p>Evalúa direcciones IP para identificar servidores maliciosos, botnets y otras amenazas de red potenciales.</p>
                <v-list density="compact" class="bg-transparent pa-0 mt-2">
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Reputación de IP</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Detección de botnets</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0">
                    <div class="text-body-2">Geolocalización de amenazas</div>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

      <!-- Statistics Section -->
      <v-sheet color="grey-lighten-3" class="py-12">
        <v-container>
          <v-row>
            <v-col cols="12" md="3" class="text-center">
              <h3 class="text-h2 font-weight-bold text-deep-purple">1M+</h3>
              <p class="text-subtitle-1">Amenazas detectadas</p>
            </v-col>
            <v-col cols="12" md="3" class="text-center">
              <h3 class="text-h2 font-weight-bold text-deep-purple">50K+</h3>
              <p class="text-subtitle-1">Usuarios activos</p>
            </v-col>
            <v-col cols="12" md="3" class="text-center">
              <h3 class="text-h2 font-weight-bold text-deep-purple">99.8%</h3>
              <p class="text-subtitle-1">Precisión en detección</p>
            </v-col>
            <v-col cols="12" md="3" class="text-center">
              <h3 class="text-h2 font-weight-bold text-deep-purple">24/7</h3>
              <p class="text-subtitle-1">Soporte técnico</p>
            </v-col>
          </v-row>
        </v-container>
      </v-sheet>

      <!-- CTA Section -->
      <!-- <v-container class="py-12">
        <v-row justify="center">
          <v-col cols="12" md="10">
            <v-card color="deep-purple" dark class="text-center pa-8 rounded-xl">
              <h2 class="text-h4 font-weight-bold mb-4">¿Listo para proteger tus sistemas?</h2>
              <p class="text-h6 mb-6">
                Comienza ahora y mantén tus archivos, navegación y red seguros contra amenazas
              </p>
              <v-btn 
                color="white" 
                size="large" 
                variant="elevated" 
                class="text-deep-purple px-6"
              >
                Comenzar prueba gratuita
              </v-btn>
            </v-card>
          </v-col>
        </v-row>
      </v-container> -->
    </v-main>

    <v-footer class="bg-deep-purple text-white">
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <div class="d-flex align-center mb-4">
              <v-icon icon="mdi-shield-lock" size="large" class="mr-2"></v-icon>
              <span class="text-h5 font-weight-bold">SecureAnalyzer</span>
            </div>
            <p>Tu plataforma de confianza para análisis de seguridad de archivos, URLs e IPs.</p>
          </v-col>
          <v-col cols="12" md="8">
            <v-row>
              <v-col cols="6" md="4">
                <h3 class="text-h6 mb-4">Producto</h3>
                <div class="d-flex flex-column gap-2">
                  <a href="#" class="text-white text-decoration-none">Características</a>
                  <a href="#" class="text-white text-decoration-none">Precios</a>
                  <a href="#" class="text-white text-decoration-none">Integraciones</a>
                  <a href="#" class="text-white text-decoration-none">API</a>
                </div>
              </v-col>
              <v-col cols="6" md="4">
                <h3 class="text-h6 mb-4">Recursos</h3>
                <div class="d-flex flex-column gap-2">
                  <a href="#" class="text-white text-decoration-none">Documentación</a>
                  <a href="#" class="text-white text-decoration-none">Blog</a>
                  <a href="#" class="text-white text-decoration-none">Tutoriales</a>
                  <a href="#" class="text-white text-decoration-none">Soporte</a>
                </div>
              </v-col>
              <v-col cols="12" md="4">
                <h3 class="text-h6 mb-4">Contacto</h3>
                <div class="d-flex flex-column gap-2">
                  <a href="#" class="text-white text-decoration-none">
                    <v-icon start>mdi-email</v-icon> info@secureanalyzer.com
                  </a>
                  <a href="#" class="text-white text-decoration-none">
                    <v-icon start>mdi-phone</v-icon> +1 (555) 123-4567
                  </a>
                </div>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <v-divider class="my-4 bg-white"></v-divider>
        <div class="d-flex flex-wrap justify-space-between">
          <div class="text-body-2">© {{ new Date().getFullYear() }} SecureAnalyzer. Todos los derechos reservados.</div>
          <div class="d-flex gap-2">
            <v-btn icon="mdi-twitter" variant="text" color="white" density="comfortable"></v-btn>
            <v-btn icon="mdi-linkedin" variant="text" color="white" density="comfortable"></v-btn>
            <v-btn icon="mdi-github" variant="text" color="white" density="comfortable"></v-btn>
          </div>
        </div>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      activeTab: 'file',
    };
  },
};
</script>

<style>
.v-application {
  background-color: #f5f5f5;
}

.v-sheet.bg-deep-purple {
  background: linear-gradient(135deg, #673ab7 0%, #9c27b0 100%);
}
</style>