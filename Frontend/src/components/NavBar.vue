<template>
  <div class="navbar-wrapper">
    <nav class="navbar-modern">
      <div class="navbar-container">
        <!-- Logo -->
        <div class="navbar-logo">
          <!-- Puedes reemplazar esto con tu logo -->
          <div class="logo-placeholder"></div>
        </div>

        <!-- Botón móvil -->
        <button
          class="menu-toggle"
          @click="isMenuOpen = !isMenuOpen"
          :class="{ 'active': isMenuOpen }"
          aria-label="Toggle navigation"
        >
          <span class="menu-icon"></span>
        </button>

        <!-- Contenido de la navegación -->
        <div class="navbar-content" :class="{ 'is-open': isMenuOpen }">
          <!-- Enlaces de navegación -->
          <ul class="nav-links">
            <li class="nav-item">
              <router-link to="/" class="nav-link">Inicio</router-link>
            </li>
            <li v-if="isAuthenticated" class="nav-item">
              <router-link to="/analisis" class="nav-link">Análisis</router-link>
            </li>
            <li v-if="isAuthenticated" class="nav-item">
              <router-link to="/advancedAnalysis" class="nav-link">Análisis Avanzado</router-link>
            </li>
          </ul>

          <!-- Área de autenticación (Desktop) -->
          <div class="auth-area">
            <button
              v-if="!isAuthenticated && !isLoading"
              id="qsLoginBtn"
              class="btn-login"
              @click.prevent="login"
            >
              Iniciar Sesión
            </button>

            <div v-if="isAuthenticated" class="profile-dropdown">
              <a
                href="#"
                class="dropdown-trigger"
                id="profileDropDown"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                <img
                  :src="user.picture"
                  alt="Foto de perfil"
                  class="profile-picture"
                />
                <span class="dropdown-arrow"></span>
              </a>
              
              <div class="dropdown-menu dropdown-menu-right">
                <div class="dropdown-header">{{ user.name }}</div>
                <router-link to="/profile" class="dropdown-item">
                  <font-awesome-icon class="mr-3" icon="user" />Perfil
                </router-link>
                <a id="qsLogoutBtn" href="#" class="dropdown-item" @click.prevent="logout">
                  <font-awesome-icon class="mr-3" icon="power-off" />Cerrar Sesión
                </a>
              </div>
            </div>
          </div>

          <!-- Área de autenticación (Móvil) -->
          <div class="mobile-auth" v-if="isMenuOpen">
            <button
              v-if="!isAuthenticated && !isLoading"
              id="qsLoginBtn"
              class="btn-login-mobile"
              @click="login"
            >
              Iniciar Sesión
            </button>

            <div v-if="isAuthenticated" class="mobile-profile">
              <div class="profile-info">
                <img
                  :src="user.picture"
                  alt="Foto de perfil"
                  class="profile-picture"
                />
                <h6>{{ user.name }}</h6>
              </div>
              <div class="mobile-actions">
                <router-link to="/profile" class="mobile-action-item">
                  <font-awesome-icon class="mr-3" icon="user" />Perfil
                </router-link>
                <a id="qsLogoutBtn" href="#" class="mobile-action-item" @click.prevent="logout">
                  <font-awesome-icon class="mr-3" icon="power-off" />Cerrar Sesión
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  name: "NavBar",
  setup() {
    const auth0 = useAuth0();
    const isMenuOpen = ref(false);
    
    return {
      isAuthenticated: auth0.isAuthenticated,
      isLoading: auth0.isLoading,
      user: auth0.user,
      isMenuOpen,
      login() {
        auth0.loginWithRedirect();
      },
      logout() {
        auth0.logout({
          logoutParams: {
            returnTo: window.location.origin
          }
        });
      }
    }
  }
};
</script>

<style>
.navbar-wrapper {
  width: 100%;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.navbar-modern {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  padding: 0.8rem 0;
  backdrop-filter: blur(10px);
}

.navbar-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.navbar-logo {
  display: flex;
  align-items: center;
}

.logo-placeholder {
  width: 40px;
  height: 40px;
  background: linear-gradient(45deg, #3498db, #8e44ad);
  border-radius: 8px;
}

/* Menu toggle para móvil */
.menu-toggle {
  display: none;
  background: transparent;
  border: none;
  width: 40px;
  height: 40px;
  position: relative;
  cursor: pointer;
}

.menu-icon {
  position: relative;
  display: block;
  width: 24px;
  height: 2px;
  background-color: #333;
  transition: all 0.3s;
}

.menu-icon::before,
.menu-icon::after {
  content: '';
  position: absolute;
  width: 24px;
  height: 2px;
  background-color: #333;
  transition: all 0.3s;
}

.menu-icon::before {
  transform: translateY(-8px);
}

.menu-icon::after {
  transform: translateY(8px);
}

/* Animación del menú */
.menu-toggle.active .menu-icon {
  background-color: transparent;
}

.menu-toggle.active .menu-icon::before {
  transform: translateY(0) rotate(45deg);
}

.menu-toggle.active .menu-icon::after {
  transform: translateY(0) rotate(-45deg);
}

/* Contenido principal de navbar */
.navbar-content {
  display: flex;
  align-items: center;
  flex-grow: 1;
  justify-content: space-between;
}

/* Enlaces de navegación */
.nav-links {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-item {
  margin: 0 0.8rem;
}

.nav-link {
  color: #333;
  text-decoration: none;
  font-weight: 500;
  position: relative;
  padding: 0.5rem 0;
  transition: color 0.3s;
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #3498db;
  transition: width 0.3s ease;
}

.nav-link:hover {
  color: #3498db;
}

.nav-link:hover::after,
.router-link-active::after {
  width: 100%;
}

.router-link-active {
  color: #3498db;
}

/* Área de autenticación */
.auth-area {
  display: flex;
  align-items: center;
}

.btn-login {
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

.btn-login:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Dropdown del perfil */
.profile-dropdown {
  position: relative;
}

.dropdown-trigger {
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 0.3rem;
  text-decoration: none;
}

.profile-picture {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #3498db;
  transition: transform 0.3s ease;
}

.dropdown-trigger:hover .profile-picture {
  transform: scale(1.05);
}

.dropdown-arrow {
  margin-left: 0.5rem;
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 5px solid #333;
}

/* Estilos del dropdown compatibles con Bootstrap */
.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  width: 220px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  z-index: 10;
  display: none;
  padding: 0.5rem 0;
  margin: 0.5rem 0 0;
  border: 1px solid rgba(0, 0, 0, 0.1);
}

.dropdown-menu-right {
  right: 0;
  left: auto;
}

.dropdown-menu.show {
  display: block;
}

.dropdown-header {
  padding: 0.75rem 1rem;
  font-weight: 600;
  border-bottom: 1px solid #eee;
  color: #333;
  font-size: 0.9rem;
}

.dropdown-item {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  color: #555;
  text-decoration: none;
  transition: background 0.2s;
  white-space: nowrap;
  font-size: 0.9rem;
}

.dropdown-item:hover {
  background: #f8f9fa;
  color: #3498db;
  text-decoration: none;
}

.mr-3 {
  margin-right: 0.75rem;
}

/* Estilos para móvil */
@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }

  .navbar-content {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: white;
    flex-direction: column;
    align-items: flex-start;
    padding: 1rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transform: translateY(-100%);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
  }

  .navbar-content.is-open {
    transform: translateY(0);
    opacity: 1;
    visibility: visible;
  }

  .nav-links {
    flex-direction: column;
    width: 100%;
  }

  .nav-item {
    margin: 0;
    width: 100%;
    border-bottom: 1px solid #eee;
  }

  .nav-link {
    display: block;
    padding: 1rem 0;
  }

  .auth-area {
    display: none;
  }

  .mobile-auth {
    width: 100%;
    margin-top: 1rem;
  }

  .btn-login-mobile {
    width: 100%;
    background: linear-gradient(45deg, #3498db, #8e44ad);
    color: white;
    border: none;
    padding: 0.8rem;
    border-radius: 8px;
    font-weight: 500;
    cursor: pointer;
  }

  .mobile-profile {
    width: 100%;
  }

  .profile-info {
    display: flex;
    align-items: center;
    padding: 1rem 0;
    border-bottom: 1px solid #eee;
  }

  .profile-info h6 {
    margin: 0 0 0 1rem;
    font-weight: 600;
  }

  .mobile-actions {
    margin-top: 0.5rem;
  }

  .mobile-action-item {
    display: flex;
    align-items: center;
    padding: 0.8rem 0;
    color: #555;
    text-decoration: none;
    border-bottom: 1px solid #eee;
  }

  .mobile-action-item:hover {
    color: #3498db;
  }
}
</style>