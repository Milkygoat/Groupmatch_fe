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
import { Loader2, UserPlus, Users, GraduationCap, CheckCircle } from 'lucide-vue-next'

const router = useRouter()
const authStore = useAuthStore()
const { toast } = useToast()

const formData = ref({
  email: '',
  password: '',
  confirmPassword: ''
})
const loading = ref(false)

const handleRegister = async () => {
  if (formData.value.password !== formData.value.confirmPassword) {
    toast({
      title: 'Password tidak cocok',
      description: 'Pastikan konfirmasi password sama dengan password.',
      variant: 'destructive'
    })
    return
  }

  loading.value = true

  const result = await authStore.register({
    email: formData.value.email,
    password: formData.value.password
  })

  if (result.success) {
    localStorage.setItem('pendingProfileSetupEmail', formData.value.email.toLowerCase())
    toast({
      title: 'Pendaftaran Berhasil',
      description: 'Akun Anda telah dibuat. Silakan login untuk melengkapi profil.',
    })
    router.push('/login')
  } else {
    toast({
      title: 'Pendaftaran Gagal',
      description: result.error || 'Terjadi kesalahan saat mendaftar.',
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
          <GraduationCap class="h-7 w-7 text-emerald-100" />
        </div>
        <h1 class="text-4xl font-semibold leading-tight">Mulai dari profil kecil, lanjut ke tim yang cocok.</h1>
        <p class="mt-4 text-sm leading-6 text-emerald-100">
          Daftar, lengkapi role dan skill, lalu biarkan GroupMatch membantu mencari tim yang lebih seimbang.
        </p>
      </div>

      <div class="grid gap-3">
        <div class="flex items-center gap-3 rounded-2xl bg-white/10 p-4 ring-1 ring-white/10">
          <CheckCircle class="h-5 w-5 text-emerald-200" />
          <p class="text-sm text-emerald-50">Cocok untuk tugas kelas, praktikum, dan project akhir.</p>
        </div>
        <div class="flex items-center gap-3 rounded-2xl bg-white/10 p-4 ring-1 ring-white/10">
          <CheckCircle class="h-5 w-5 text-emerald-200" />
          <p class="text-sm text-emerald-50">Skill dan kebutuhan tim terlihat lebih jelas.</p>
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
          <h1 class="text-2xl font-semibold text-slate-900">Daftar GroupMatch</h1>
          <CardTitle class="pt-2 text-xl font-semibold text-slate-900">Buat akun mahasiswa</CardTitle>
          <CardDescription class="text-sm leading-6 text-slate-500">
            Daftar cukup dengan email, lalu lengkapi profil setelah login.
          </CardDescription>
        </CardHeader>

      <CardContent class="space-y-4 pt-4">
        <form @submit.prevent="handleRegister" class="space-y-3">
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
          <div class="grid grid-cols-1 gap-3 sm:grid-cols-2">
            <div class="space-y-2">
              <Label for="password" class="text-slate-700">Password</Label>
              <Input
                id="password"
                type="password"
                v-model="formData.password"
                required
                class="h-11 rounded-xl border-emerald-100 bg-slate-50 transition-colors focus:bg-white"
              />
            </div>
            <div class="space-y-2">
              <Label for="confirmPassword" class="text-slate-700">Konfirmasi</Label>
              <Input
                id="confirmPassword"
                type="password"
                v-model="formData.confirmPassword"
                required
                class="h-11 rounded-xl border-emerald-100 bg-slate-50 transition-colors focus:bg-white"
              />
            </div>
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
              <UserPlus class="mr-2 h-4 w-4" /> Daftar
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
          Daftar dengan Google
        </Button>
      </CardContent>

      <CardFooter class="flex flex-col space-y-4 pt-2">
        <div class="text-center text-sm text-slate-500">
          Sudah punya akun?
          <a
            href="#"
            @click.prevent="navigateTo('/login')"
            class="font-medium text-emerald-700 hover:text-emerald-800 hover:underline"
          >
            Masuk sekarang
          </a>
        </div>
      </CardFooter>
    </Card>
    </section>
  </div>
</template>
