<script setup>
import { computed } from 'vue'
import { cn } from '@/lib/utils'

const props = defineProps({
  variant: {
    type: String,
    default: 'default',
    validator: (v) => ['default', 'destructive', 'outline', 'secondary', 'ghost', 'link'].includes(v)
  },
  size: {
    type: String,
    default: 'default',
    validator: (v) => ['default', 'sm', 'lg', 'icon'].includes(v)
  },
  disabled: Boolean,
  class: String
})

const emit = defineEmits(['click'])

const variants = {
  default: 'bg-emerald-600 text-white hover:bg-emerald-700',
  destructive: 'bg-red-500 text-slate-50 hover:bg-red-500/90',
  outline: 'border border-slate-200 bg-white hover:bg-emerald-50 hover:text-emerald-800',
  secondary: 'bg-emerald-50 text-emerald-800 hover:bg-emerald-100',
  ghost: 'hover:bg-emerald-50 hover:text-emerald-800',
  link: 'text-emerald-700 underline-offset-4 hover:underline'
}

const sizes = {
  default: 'h-10 px-4 py-2',
  sm: 'h-9 rounded-md px-3',
  lg: 'h-11 rounded-md px-8',
  icon: 'h-10 w-10'
}

const buttonClass = computed(() =>
  cn(
    'inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-white transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-600 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
    variants[props.variant],
    sizes[props.size],
    props.class
  )
)
</script>

<template>
  <button
    :class="buttonClass"
    :disabled="disabled"
    @click="$emit('click', $event)"
  >
    <slot />
  </button>
</template>
