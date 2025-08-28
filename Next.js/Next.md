# NEXT.JS

1. npx create-next-app@latest --empty
2. Would you like to use TypeScript? **Yes**
3. Which linter would you like to use? › **ESLint**
4. Would you like to use Tailwind CSS? **No**
5. Would you like your code inside a `src/` directory? **Yes**
6. Would you like to use App Router? (recommended) **Yes**
7. Would you like to use Turbopack? (recommended) **Yes**
8. Would you like to customize the import alias (`@/*` by default)? **No**
9. cd my-app
10. npm install tailwindcss @tailwindcss/postcss postcss
11. Criar o postcss.config.mjs (Colocar o código depois)
'''
const config = {
    plugins: {
        "@tailwindcss/postcss": {},
    },
};

export default config;
'''tsx
12. globals.css (dentro da pasta app) e colocar o **@import 'tailwindcss';**
13. Adicionar no layout.tsx (dentro da pasta app) o **import './globals.css'**
11. npx shadcn@latest init


**Extensões Importante: Tailwind CSS IntelliSense, Prettier e Colorize**

**O Prettier no linux funciona com _ctrl+shift+i_**

**LEMBRANDO QUE PARA RODAR É SÓ METER _npm run dev_**