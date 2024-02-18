## zh-CN

最简单的用法。

## en-US

The most basic usage.

```css
.site-back-top-basic {
  color: rgba(64, 64, 64, 0.6);
}
```
```tsx
import React from 'react';
import { BackTop } from 'antd';

const App: React.FC = () => (
  <>
    <BackTop />
    Scroll down to see the bottom-right
    <strong className="site-back-top-basic"> gray </strong>
    button.
  </>
);

export default App;
```
