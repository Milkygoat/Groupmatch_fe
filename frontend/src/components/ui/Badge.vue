<script setup>
import { computed } from 'vue'
import { cn } from '@/lib/utils'

const props = defineProps({
  class: String,
  variant: {
    type: String,
    default: 'default',
    validator: (v) => ['default', 'secondary', 'destructive', 'outline'].includes(v)
  }
})

const variants = {
  default: 'border-transparent bg-emerald-600 text-white hover:bg-emerald-700',
  secondary: 'border-transparent bg-emerald-50 text-emerald-800 hover:bg-emerald-100',
  destructive: 'border-transparent bg-red-500 text-slate-50 hover:bg-red-500/80',
  outline: 'border-emerald-200 bg-white text-emerald-700'
}

const badgeClass = computed(() =>
  cn(
    'inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2',
    variants[props.variant],
    props.class
  )
)
</script>

<template>
  <div :class="badgeClass">
    <slot />
  </div>
</template>
