<script setup>
import { useRouter } from 'vue-router'
import Button from '@/components/ui/Button.vue'
import Card from '@/components/ui/Card.vue'
import CardContent from '@/components/ui/CardContent.vue'
import {
  Users,
  ArrowRight,
  Target,
  MessageSquare,
  Shield,
  CheckCircle,
  BookOpen,
  GraduationCap,
  Sparkles,
  Clock3,
  Layers3,
} from 'lucide-vue-next'

const router = useRouter()

const features = [
  {
    icon: Target,
    title: 'Matching berdasarkan skill',
    description: 'Role, minat, dan kemampuan anggota dibuat lebih mudah terbaca sebelum mulai kerja kelompok.',
  },
  {
    icon: MessageSquare,
    title: 'Room diskusi langsung',
    description: 'Begitu tim terbentuk, anggota bisa langsung koordinasi di satu ruang chat yang fokus.',
  },
  {
    icon: Shield,
    title: 'Profil yang relevan',
    description: 'Data yang diminta hanya yang membantu proses pencarian tim dan kolaborasi belajar.',
  },
]

const steps = [
  'Lengkapi profil dan skill',
  'Mulai pencarian tim',
  'Masuk room dan diskusi',
]

const navigateTo = (path) => {
  router.push(path)
}
</script>

<template>
  <div class="min-h-screen bg-[#f5faf7] text-slate-800">
    <header class="sticky top-0 z-50 border-b border-emerald-100/80 bg-[#f5faf7]/90 backdrop-blur-md">
      <div class="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6">
        <button class="flex items-center gap-3 text-left" @click="navigateTo('/')">
          <div class="flex h-10 w-10 items-center justify-center rounded-2xl bg-emerald-600 shadow-sm shadow-emerald-200">
            <Users class="h-5 w-5 text-white" />
          </div>
          <div>
            <p class="text-xl font-semibold text-slate-950">GroupMatch</p>
            <p class="hidden text-xs font-medium text-emerald-700 sm:block">student collaboration hub</p>
          </div>
        </button>

        <div class="flex items-center gap-2">
          <Button variant="ghost" class="rounded-xl text-slate-600" @click="navigateTo('/login')">
            Masuk
          </Button>
          <Button class="rounded-xl px-4 shadow-sm shadow-emerald-200" @click="navigateTo('/register')">
            Daftar Gratis
          </Button>
        </div>
      </div>
    </header>

    <main>
      <section class="mx-auto grid max-w-7xl items-center gap-10 px-4 py-12 sm:px-6 lg:grid-cols-[1fr_0.92fr] lg:py-20">
        <div>
          <div class="mb-5 inline-flex items-center gap-2 rounded-full border border-emerald-100 bg-white px-4 py-2 text-sm font-medium text-emerald-700 shadow-sm">
            <GraduationCap class="h-4 w-4" />
            Dirancang untuk tugas, project, dan praktikum
          </div>

          <h1 class="max-w-3xl text-4xl font-semibold leading-tight tracking-normal text-slate-950 sm:text-5xl lg:text-6xl">
            Bentuk tim kuliah yang seimbang tanpa ribet.
          </h1>

          <p class="mt-5 max-w-2xl text-base leading-7 text-slate-600 sm:text-lg">
            GroupMatch membantu mahasiswa menemukan partner kerja kelompok berdasarkan skill dan role, lalu langsung lanjut koordinasi di room yang sama.
          </p>

          <div class="mt-8 flex flex-col gap-3 sm:flex-row">
            <Button
              size="lg"
              class="h-12 rounded-xl px-7 text-base shadow-sm shadow-emerald-200"
              @click="navigateTo('/register')"
            >
              Mulai Cari Tim <ArrowRight class="ml-2 h-4 w-4" />
            </Button>
            <Button
              size="lg"
              variant="outline"
              class="h-12 rounded-xl border-emerald-200 px-7 text-base"
              @click="navigateTo('/login')"
            >
              Saya Sudah Punya Akun
            </Button>
          </div>
        </div>

        <div class="rounded-[2rem] border border-emerald-100 bg-white p-4 shadow-xl shadow-emerald-100/60">
          <div class="rounded-[1.5rem] bg-emerald-900 p-5 text-white">
            <div class="flex items-center justify-between border-b border-white/10 pb-4">
              <div>
                <p class="text-sm font-medium text-emerald-200">Matching Preview</p>
                <h2 class="mt-1 text-xl font-semibold">Project Komputasi Awan</h2>
              </div>
              <div class="rounded-2xl bg-emerald-400/15 p-3 text-emerald-200">
                <Sparkles class="h-6 w-6" />
              </div>
            </div>

            <div class="mt-5 grid gap-3">
              <div class="rounded-2xl bg-white/10 p-4 ring-1 ring-white/10">
                <div class="flex items-start justify-between gap-3">
                  <div>
                    <p class="text-sm font-semibold">Tim Backend API</p>
                    <p class="mt-1 text-xs leading-5 text-slate-300">Butuh 1 UI/UX dan 1 Frontend untuk demo akhir.</p>
                  </div>
                  <span class="rounded-full bg-emerald-300 px-2.5 py-1 text-xs font-semibold text-emerald-950">92%</span>
                </div>
                <div class="mt-4 flex flex-wrap gap-2">
                  <span class="rounded-full bg-white/10 px-3 py-1 text-xs text-slate-200">Vue</span>
                  <span class="rounded-full bg-white/10 px-3 py-1 text-xs text-slate-200">Figma</span>
                  <span class="rounded-full bg-white/10 px-3 py-1 text-xs text-slate-200">API</span>
                </div>
              </div>

              <div class="grid grid-cols-3 gap-3">
                <div class="rounded-2xl bg-white/10 p-3">
                  <BookOpen class="h-5 w-5 text-sky-200" />
                  <p class="mt-3 text-lg font-semibold">24</p>
                  <p class="text-xs text-slate-300">skill aktif</p>
                </div>
                <div class="rounded-2xl bg-white/10 p-3">
                  <Users class="h-5 w-5 text-emerald-200" />
                  <p class="mt-3 text-lg font-semibold">4</p>
                  <p class="text-xs text-slate-300">anggota</p>
                </div>
                <div class="rounded-2xl bg-white/10 p-3">
                  <Clock3 class="h-5 w-5 text-amber-200" />
                  <p class="mt-3 text-lg font-semibold">2m</p>
                  <p class="text-xs text-slate-300">mulai</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="border-y border-emerald-100 bg-white/70">
        <div class="mx-auto grid max-w-7xl gap-4 px-4 py-6 sm:px-6 md:grid-cols-3">
          <div v-for="(step, index) in steps" :key="step" class="flex items-center gap-3">
            <div class="flex h-9 w-9 items-center justify-center rounded-xl bg-emerald-50 text-sm font-semibold text-emerald-700">
              {{ index + 1 }}
            </div>
            <p class="text-sm font-medium text-slate-700">{{ step }}</p>
          </div>
        </div>
      </section>

      <section class="mx-auto max-w-7xl px-4 py-14 sm:px-6">
        <div class="mb-7 flex items-end justify-between gap-4">
          <div>
            <p class="text-sm font-semibold text-emerald-700">Fitur utama</p>
            <h2 class="mt-2 text-3xl font-semibold text-slate-950">Semua yang dibutuhkan untuk mulai kolaborasi.</h2>
          </div>
          <Layers3 class="hidden h-10 w-10 text-emerald-500 sm:block" />
        </div>

        <div class="grid grid-cols-1 gap-5 md:grid-cols-3">
          <Card
            v-for="feature in features"
            :key="feature.title"
            class="border-emerald-100 bg-white shadow-sm shadow-emerald-100/70"
          >
            <CardContent class="p-6">
              <div class="mb-4 flex h-12 w-12 items-center justify-center rounded-2xl bg-emerald-50">
                <component :is="feature.icon" class="h-6 w-6 text-emerald-600" />
              </div>
              <h3 class="text-lg font-semibold text-slate-950">{{ feature.title }}</h3>
              <p class="mt-2 text-sm leading-6 text-slate-600">{{ feature.description }}</p>
            </CardContent>
          </Card>
        </div>
      </section>

      <section class="mx-auto max-w-7xl px-4 pb-16 sm:px-6">
        <div class="grid gap-5 rounded-[2rem] border border-emerald-100 bg-emerald-900 p-6 text-white shadow-lg shadow-emerald-100 md:grid-cols-[0.9fr_1.1fr] md:p-10">
          <div>
            <p class="text-sm font-semibold text-emerald-200">Kenapa cocok untuk mahasiswa?</p>
            <h2 class="mt-3 text-3xl font-semibold leading-tight">Alurnya pendek, hasilnya langsung bisa dipakai.</h2>
          </div>
          <div class="grid gap-3 sm:grid-cols-2">
            <div class="rounded-2xl bg-white/10 p-4 ring-1 ring-white/10">
              <CheckCircle class="h-5 w-5 text-emerald-200" />
              <p class="mt-3 text-sm leading-6 text-emerald-50">Tidak perlu mencari anggota manual dari banyak chat kelas.</p>
            </div>
            <div class="rounded-2xl bg-white/10 p-4 ring-1 ring-white/10">
              <CheckCircle class="h-5 w-5 text-emerald-200" />
              <p class="mt-3 text-sm leading-6 text-emerald-50">Skill dan role terlihat jelas sebelum diskusi dimulai.</p>
            </div>
          </div>
        </div>
      </section>
    </main>

    <footer class="border-t border-emerald-100 bg-white py-8">
      <div class="mx-auto flex max-w-7xl flex-col items-center justify-between gap-3 px-4 text-sm text-slate-500 sm:flex-row sm:px-6">
        <div class="flex items-center gap-2">
          <div class="flex h-8 w-8 items-center justify-center rounded-xl bg-emerald-600">
            <Users class="h-4 w-4 text-white" />
          </div>
          <span class="font-semibold text-slate-900">GroupMatch</span>
        </div>
        <p>(c) 2026 GroupMatch. Kolaborasi kampus yang lebih rapi.</p>
      </div>
    </footer>
  </div>
</template>
