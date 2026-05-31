<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useToast } from '@/composables/useToast'
import Button from '@/components/ui/Button.vue'
import Input from '@/components/ui/Input.vue'
import Label from '@/components/ui/Label.vue'
import Card from '@/components/ui/Card.vue'
import CardHeader from '@/components/ui/CardHeader.vue'
import CardTitle from '@/components/ui/CardTitle.vue'
import CardDescription from '@/components/ui/CardDescription.vue'
import CardContent from '@/components/ui/CardContent.vue'
import CardFooter from '@/components/ui/CardFooter.vue'
import { Loader2, LogIn, Users, BookOpen, CheckCircle } from 'lucide-vue-next'

const router = useRouter()
const authStore = useAuthStore()
const { toast } = useToast()

const formData = ref({
  email: '',
  password: ''
})
const loading = ref(false)

const handleLogin = async () => {
  loading.value = true

  const result = await authStore.login(formData.value.email, formData.value.password)

  if (result.success) {
    console.log('[LOGIN] Login successful, navigating to dashboard...')
    toast({
      title: 'Login Berhasil',
      description: 'Selamat datang kembali!',
    })
    setTimeout(() => {
      const pendingProfileEmail = localStorage.getItem('pendingProfileSetupEmail')
      const loginEmail = formData.value.email.toLowerCase()

      // Only redirect to profile setup for newly registered users
      if (pendingProfileEmail === loginEmail) {
        localStorage.removeItem('pendingProfileSetupEmail')
        router.push('/profile-setup')
      } else {
        router.push('/dashboard')
      }
    }, 100)
  } else {
    console.log('[LOGIN] Login failed:', result.error)
    toast({
      title: 'Login Gagal',
      description: result.error || 'Email atau password salah.',
      variant: 'destructive'
    })
    loading.value = false
  }
}

const handleGoogleLogin = async () => {
  try {
    await authStore.loginWithGoogle()
  } catch (error) {
    console.error('Google login error:', error)
    toast({
      title: 'Error',
      description: 'Gagal memuat login Google.',
      variant: 'destructive'
    })
  }
}

const navigateTo = (path) => {
  router.push(path)
}
</script>

<template>
  <div class="grid min-h-screen bg-[#f5faf7] lg:grid-cols-[0.95fr_1.05fr]">
    <section class="hidden border-r border-emerald-100 bg-emerald-900 p-10 text-white lg:flex lg:flex-col lg:justify-between">
      <div class="flex items-center gap-3">
        <div class="flex h-11 w-11 items-center justify-center rounded-2xl bg-white/10 ring-1 ring-white/15">
          <Users class="h-6 w-6 text-emerald-100" />
        </div>
        <div>
          <p class="text-xl font-semibold">GroupMatch</p>
          <p class="text-xs text-emerald-200">student collaboration hub</p>
        </div>
      </div>

      <div class="max-w-md">
        <div class="mb-5 flex h-14 w-14 items-center justify-center rounded-2xl bg-white/10 ring-1 ring-white/10">
          <BookOpen class="h-7 w-7 text-emerald-100" />
        </div>
        <h1 class="text-4xl font-semibold leading-tight">Lanjutkan kerja kelompokmu dari satu tempat.</h1>
        <p class="mt-4 text-sm leading-6 text-emerald-100">
          Masuk untuk melihat status tim, room aktif, dan riwayat kolaborasi yang sudah kamu buat.
        </p>
      </div>

      <div class="grid gap-3">
        <div class="flex items-center gap-3 rounded-2xl bg-white/10 p-4 ring-1 ring-white/10">
          <CheckCircle class="h-5 w-5 text-emerald-200" />
          <p class="text-sm text-emerald-50">Profil skill tersimpan dan siap dipakai matching.</p>
        </div>
        <div class="flex items-center gap-3 rounded-2xl bg-white/10 p-4 ring-1 ring-white/10">
          <CheckCircle class="h-5 w-5 text-emerald-200" />
          <p class="text-sm text-emerald-50">Room tim tetap bisa dibuka dari dashboard.</p>
        </div>
      </div>
    </section>

    <section class="flex items-center justify-center px-4 py-8">
      <Card class="relative z-10 w-full max-w-md rounded-[1.5rem] border-emerald-100 bg-white shadow-xl shadow-emerald-100/50">
        <CardHeader class="space-y-1 pb-2 text-center">
          <div class="mx-auto mb-4 lg:hidden">
            <div class="flex h-16 w-16 items-center justify-center rounded-2xl bg-emerald-600 shadow-sm shadow-emerald-200">
              <Users class="h-8 w-8 text-white" />
            </div>
          </div>
          <h1 class="text-2xl font-semibold text-slate-900">Masuk ke GroupMatch</h1>
          <CardTitle class="pt-2 text-xl font-semibold text-slate-900">Selamat datang kembali</CardTitle>
          <CardDescription class="text-sm leading-6 text-slate-500">
            Gunakan akunmu untuk lanjut mencari dan mengelola tim kampus.
          </CardDescription>
        </CardHeader>
      
      <CardContent class="space-y-4 pt-4">
        <form @submit.prevent="handleLogin" class="space-y-4">
          <div class="space-y-2">
            <Label for="email" class="text-slate-700">Email</Label>
            <Input
              id="email"
              type="email"
              placeholder="nama@email.com"
              v-model="formData.email"
              required
              class="h-11 rounded-xl border-emerald-100 bg-slate-50 transition-colors focus:bg-white"
            />
          </div>
          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <Label for="password" class="text-slate-700">Password</Label>
              <a href="#" class="text-xs text-emerald-700 hover:text-emerald-800 hover:underline">
                Lupa password?
              </a>
            </div>
            <Input
              id="password"
              type="password"
              v-model="formData.password"
              required
              class="h-11 rounded-xl border-emerald-100 bg-slate-50 transition-colors focus:bg-white"
            />
          </div>
          <Button
            type="submit"
            class="h-11 w-full rounded-xl bg-emerald-600 text-white shadow-sm shadow-emerald-200 hover:bg-emerald-700"
            :disabled="loading"
          >
            <template v-if="loading">
              <Loader2 class="mr-2 h-4 w-4 animate-spin" />
              Memproses...
            </template>
            <template v-else>
              <LogIn class="mr-2 h-4 w-4" /> Masuk
            </template>
          </Button>
        </form>

        <div class="relative my-6">
          <div class="absolute inset-0 flex items-center">
            <span class="w-full border-t border-slate-200" />
          </div>
          <div class="relative flex justify-center text-xs uppercase">
            <span class="bg-white px-3 text-slate-400">atau</span>
          </div>
        </div>

        <Button
          variant="outline"
          type="button"
          class="h-11 w-full rounded-xl border-slate-200 hover:bg-slate-50"
          @click="handleGoogleLogin"
        >
          <svg class="mr-2 h-4 w-4" viewBox="0 0 488 512">
            <path fill="currentColor" d="M488 261.8C488 403.3 391.1 504 248 504 110.8 504 0 393.2 0 256S110.8 8 248 8c66.8 0 123 24.5 166.3 64.9l-67.5 64.9C258.5 52.6 94.3 116.6 94.3 256c0 86.5 69.1 156.6 153.7 156.6 98.2 0 135-70.4 140.8-106.9H248v-85.3h236.1c2.3 12.7 3.9 24.9 3.9 41.4z"/>
          </svg>
          Masuk dengan Google
        </Button>
      </CardContent>

      <CardFooter class="flex flex-col space-y-4 pt-2">
        <div class="text-center text-sm text-slate-500">
          Belum punya akun?
          <a
            href="#"
            @click.prevent="navigateTo('/register')"
            class="font-medium text-emerald-700 hover:text-emerald-800 hover:underline"
          >
            Daftar sekarang
          </a>
        </div>
      </CardFooter>
    </Card>
    </section>
  </div>
</template>
