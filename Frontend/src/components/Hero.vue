<template>
  <v-app>
    <v-main>
      <v-container fluid class="pa-0">
        <v-row no-gutters>
          <v-col cols="12">
            <div class="hero-section">
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
                        class="primary-btn"
                        elevation="1"
                      >
                        <v-icon start>mdi-rocket-launch</v-icon>
                        Comenzar ahora
                      </v-btn>
                      <v-btn
                        size="large"
                        class="secondary-btn"
                        variant="outlined"
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
                      class="rounded-lg elevation-3"
                      max-width="500"
                    ></v-img>
                  </v-col>
                </v-row>
              </v-container>
            </div>
          </v-col>
        </v-row>
      </v-container>

      <v-container class="py-12">
        <v-row class="mb-6">
          <v-col cols="12" class="text-center">
            <h2 class="text-h3 font-weight-bold mb-2">Características principales</h2>
            <p class="text-subtitle-1">Descubre cómo nuestra plataforma te mantiene seguro</p>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="4">
            <v-card height="100%" class="feature-card pa-6" variant="elevated" elevation="2">
              <div class="feature-icon mb-4">
                <v-icon icon="mdi-file-search-outline" size="42" color="#3498db"></v-icon>
              </div>
              <v-card-title class="text-h5 pa-0 font-weight-bold">Análisis de archivos</v-card-title>
              <v-card-text class="pa-0 pt-2">
                <p>Detecta malware, virus, ransomware y otras amenazas en tus archivos antes de abrirlos. Compatible con múltiples formatos.</p>
                <v-list density="compact" class="bg-transparent pa-0 mt-4">
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Escaneo de virus y malware</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Detección de código malicioso</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Verificación de firma digital</div>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" md="4">
            <v-card height="100%" class="feature-card pa-6" variant="elevated" elevation="2">
              <div class="feature-icon mb-4">
                <v-icon icon="mdi-web-check" size="42" color="#3498db"></v-icon>
              </div>
              <v-card-title class="text-h5 pa-0 font-weight-bold">Análisis de URLs</v-card-title>
              <v-card-text class="pa-0 pt-2">
                <p>Verifica la seguridad de enlaces y sitios web antes de visitarlos para protegerte contra phishing y sitios maliciosos.</p>
                <v-list density="compact" class="bg-transparent pa-0 mt-4">
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Detección de phishing</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Verificación de certificados SSL</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Evaluación de contenido malicioso</div>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" md="4">
            <v-card height="100%" class="feature-card pa-6" variant="elevated" elevation="2">
              <div class="feature-icon mb-4">
                <v-icon icon="mdi-ip-network-outline" size="42" color="#3498db"></v-icon>
              </div>
              <v-card-title class="text-h5 pa-0 font-weight-bold">Análisis de IPs</v-card-title>
              <v-card-text class="pa-0 pt-2">
                <p>Evalúa direcciones IP para identificar servidores maliciosos, botnets y otras amenazas de red potenciales.</p>
                <v-list density="compact" class="bg-transparent pa-0 mt-4">
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Reputación de IP</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Detección de botnets</div>
                  </v-list-item>
                  <v-list-item prepend-icon="mdi-check" class="pa-0 feature-list-item">
                    <div class="text-body-2">Geolocalización de amenazas</div>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

      <v-sheet color="grey-lighten-3" class="py-12 stats-section">
        <v-container>
          <v-row>
            <v-col cols="12" md="3" class="text-center">
              <h3 class="text-h2 font-weight-bold gradient-text">1M+</h3>
              <p class="text-subtitle-1">Amenazas detectadas</p>
            </v-col>
            <v-col cols="12" md="3" class="text-center">
              <h3 class="text-h2 font-weight-bold gradient-text">50K+</h3>
              <p class="text-subtitle-1">Usuarios activos</p>
            </v-col>
            <v-col cols="12" md="3" class="text-center">
              <h3 class="text-h2 font-weight-bold gradient-text">99.8%</h3>
              <p class="text-subtitle-1">Precisión en detección</p>
            </v-col>
            <v-col cols="12" md="3" class="text-center">
              <h3 class="text-h2 font-weight-bold gradient-text">24/7</h3>
              <p class="text-subtitle-1">Soporte técnico</p>
            </v-col>
          </v-row>
        </v-container>
      </v-sheet>

      <v-container class="py-12">
        <v-row justify="center">
          <v-col cols="12" md="10">
            <v-card class="cta-card text-center pa-8 rounded-xl" elevation="3">
              <h2 class="text-h4 font-weight-bold mb-4 text-white">¿Listo para proteger tus sistemas?</h2>
              <p class="text-h6 mb-6 text-white">
                Comienza ahora y mantén tus archivos, navegación y red seguros contra amenazas
              </p>
              <v-btn 
                class="cta-btn"
                size="large" 
                elevation="1"
                rounded="pill"
              >
                Comenzar prueba gratuita
              </v-btn>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>

    <v-footer class="footer-gradient text-white">
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
                <h3 class="text-h6 mb-4 font-weight-bold">Producto</h3>
                <div class="d-flex flex-column gap-2">
                  <a href="#" class="footer-link">Características</a>
                  <a href="#" class="footer-link">Precios</a>
                  <a href="#" class="footer-link">Integraciones</a>
                  <a href="#" class="footer-link">API</a>
                </div>
              </v-col>
              <v-col cols="6" md="4">
                <h3 class="text-h6 mb-4 font-weight-bold">Recursos</h3>
                <div class="d-flex flex-column gap-2">
                  <a href="#" class="footer-link">Documentación</a>
                  <a href="#" class="footer-link">Blog</a>
                  <a href="#" class="footer-link">Tutoriales</a>
                  <a href="#" class="footer-link">Soporte</a>
                </div>
              </v-col>
              <v-col cols="12" md="4">
                <h3 class="text-h6 mb-4 font-weight-bold">Contacto</h3>
                <div class="d-flex flex-column gap-2">
                  <a href="#" class="footer-link">
                    <v-icon start size="small">mdi-email</v-icon> info@secureanalyzer.com
                  </a>
                  <a href="#" class="footer-link">
                    <v-icon start size="small">mdi-phone</v-icon> +1 (555) 123-4567
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
:root {
  --primary-gradient: linear-gradient(45deg, #3498db, #8e44ad);
  --primary-color: #3498db;
  --secondary-color: #8e44ad;
  --text-dark: #333;
  --text-light: #555;
  --card-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  --hover-transition: all 0.3s ease;
}

.v-application {
  background-color: #f5f5f5;
}

.hero-section {
  
  background: linear-gradient(45deg, #3498db, #8e44ad);
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 24px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.primary-btn {
  background: white !important;
  color: var(--primary-color) !important;
  border-radius: 24px !important;
  font-weight: 500 !important;
  transition: var(--hover-transition);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1) !important;
}

.primary-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
}

.secondary-btn {
  background: transparent !important;
  color: white !important;
  border: 2px solid rgba(255, 255, 255, 0.7) !important;
  border-radius: 24px !important;
  font-weight: 500 !important;
  transition: var(--hover-transition);
}

.secondary-btn:hover {
  background: rgba(255, 255, 255, 0.1) !important;
  transform: translateY(-2px);
}

.feature-card {
  border-radius: 12px !important;
  transition: var(--hover-transition);
  border: 1px solid rgba(0, 0, 0, 0.05) !important;
  overflow: hidden;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1) !important;
}

.feature-icon {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 70px;
  height: 70px;
  border-radius: 12px;
  background: rgba(52, 152, 219, 0.1);
}

.feature-list-item {
  padding-top: 8px !important;
  padding-bottom: 8px !important;
}

.feature-list-item .v-icon {
  color: var(--primary-color) !important;
}

.stats-section {
  background-color: #f8f9fa !important;
  border-top: 1px solid rgba(0, 0, 0, 0.05);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.gradient-text {
  background: var(--primary-gradient);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.cta-card {
  background: var(--primary-gradient) !important;
  border: none !important;
}

.cta-btn {
  background: white !important;
  color: #8e44ad !important;
  font-weight: 600 !important;
  padding: 0 24px !important;
  height: 48px !important;
  transition: var(--hover-transition);
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important;
}

.footer-gradient {
  background: var(--primary-gradient) !important;
  padding-top: 4rem;
  padding-bottom: 2rem;
}

.footer-link {
  color: rgba(255, 255, 255, 0.8) !important;
  text-decoration: none;
  transition: color 0.2s;
  display: inline-flex;
  align-items: center;
  padding: 4px 0;
}

.footer-link:hover {
  color: white !important;
  text-decoration: none;
}
.feature-list-item {
  padding-top: 8px;
  padding-bottom: 8px;
}

@media (max-width: 768px) {
  .v-row {
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
}
</style>