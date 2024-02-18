---
category: Components
group: 反馈
title: Spin
subtitle: 加载中
cover: https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*5mC5TomY4B0AAAAAAAAAAAAADrJ8AQ/original
coverDark: https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*i43_ToFrL8YAAAAAAAAAAAAADrJ8AQ/original
demo:
  cols: 2
---

用于页面和区块的加载中状态。

## 何时使用

页面局部处于等待异步数据或正在渲染过程时，合适的加载动效会有效缓解用户的焦虑。

## 代码演示

<!-- prettier-ignore -->
<code src="./demo/basic.tsx">基本用法</code>
<code src="./demo/size.tsx">各种大小</code>
<code src="./demo/inside.tsx">容器</code>
<code src="./demo/nested.tsx">卡片加载中</code>
<code src="./demo/tip.tsx">自定义描述文案</code>
<code src="./demo/delayAndDebounce.tsx">延迟</code>
<code src="./demo/custom-indicator.tsx">自定义指示符</code>
<code src="./demo/fullscreen.tsx">全屏</code>

## API

通用属性参考：[通用属性](/docs/react/common-props)

| 参数 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| delay | 延迟显示加载效果的时间（防止闪烁） | number (毫秒) | - |
| indicator | 加载指示符 | ReactNode | - |
| size | 组件大小，可选值为 `small` `default` `large` | string | `default` |
| spinning | 是否为加载中状态 | boolean | true |
| tip | 当作为包裹元素时，可以自定义描述文案 | ReactNode | - |
| wrapperClassName | 包装器的类属性 | string | - |
| fullscreen | 显示带有 `Spin` 组件的背景 | boolean | false | 5.11.0 |

### 静态方法

- `Spin.setDefaultIndicator(indicator: ReactNode)`

  你可以自定义全局默认 Spin 的元素。

## 主题变量（Design Token）

<ComponentTokenTable component="Spin"></ComponentTokenTable>

## size demo
>/demo/size.tsx


小的用于文本加载，默认用于卡片容器级加载，大的用于**页面级**加载。



A small `Spin` is used for loading text, default sized `Spin` for loading a card-level block, and large `Spin` used for loading a **page**.
```tsx
import React from 'react';
import { Flex, Spin } from 'antd';

const App: React.FC = () => (
  <Flex align="center" gap="middle">
    <Spin size="small" />
    <Spin />
    <Spin size="large" />
  </Flex>
);

export default App;
```

## inside demo
>/demo/inside.tsx


放入一个容器中。



Spin in a container.

```css
.example {
  margin: 20px 0;
  margin-bottom: 20px;
  padding: 30px 50px;
  text-align: center;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
}
```

<style>
  .example {
    background: rgba(255,255,255,0.08);
  }
</style>
```tsx
import React from 'react';
import { Spin } from 'antd';

const App: React.FC = () => (
  <div className="example">
    <Spin />
  </div>
);

export default App;
```

## custom-indicator demo
>/demo/custom-indicator.tsx


使用自定义指示符。



Use custom loading indicator.
```tsx
import React from 'react';
import { LoadingOutlined } from '@ant-design/icons';
import { Spin } from 'antd';

const App: React.FC = () => <Spin indicator={<LoadingOutlined style={{ fontSize: 24 }} spin />} />;

export default App;
```

## nested demo
>/demo/nested.tsx


可以直接把内容内嵌到 `Spin` 中，将现有容器变为加载状态。



Embedding content into `Spin` will set it into loading state.
```tsx
import React from 'react';
import { Alert, Spin, Switch } from 'antd';

const App: React.FC = () => {
  const [loading, setLoading] = React.useState<boolean>(false);
  return (
    <>
      <Spin spinning={loading}>
        <Alert
          type="info"
          message="Alert message title"
          description="Further details about the context of this alert."
        />
      </Spin>
      <div style={{ marginTop: 16 }}>
        Loading state：
        <Switch checked={loading} onChange={setLoading} />
      </div>
    </>
  );
};

export default App;
```

## delayAndDebounce demo
>/demo/delayAndDebounce.tsx


延迟显示 loading 效果。当 spinning 状态在 `delay` 时间内结束，则不显示 loading 状态。



Specifies a delay for loading state. If `spinning` ends during delay, loading status won't appear.
```tsx
import React from 'react';
import { Alert, Spin, Switch } from 'antd';

const App: React.FC = () => {
  const [loading, setLoading] = React.useState<boolean>(false);
  return (
    <>
      <Spin spinning={loading} delay={500}>
        <Alert
          type="info"
          message="Alert message title"
          description="Further details about the context of this alert."
        />
      </Spin>
      <div style={{ marginTop: 16 }}>
        Loading state：
        <Switch checked={loading} onChange={setLoading} />
      </div>
    </>
  );
};

export default App;
```

## fullscreen demo
>/demo/fullscreen.tsx


`fullscreen` 属性非常适合创建流畅的页面加载器。它添加了半透明覆盖层，并在其中心放置了一个旋转加载符号。



The `fullscreen` mode is perfect for creating page loaders. It adds a dimmed overlay with a centered spinner.
```tsx
import React from 'react';
import { Button, Spin } from 'antd';

const App: React.FC = () => {
  const [spinning, setSpinning] = React.useState<boolean>(false);

  const showLoader = () => {
    setSpinning(true);
    setTimeout(() => {
      setSpinning(false);
    }, 3000);
  };

  return (
    <>
      <Button onClick={showLoader}>Show fullscreen for 3s</Button>
      <Spin spinning={spinning} fullscreen />
    </>
  );
};

export default App;
```

## basic demo
>/demo/basic.tsx


一个简单的 loading 状态。



A simple loading status.
```tsx
import React from 'react';
import { Spin } from 'antd';

const App: React.FC = () => <Spin />;

export default App;
```

## tip demo
>/demo/tip.tsx


自定义描述文案。



```css
.content {
  padding: 50px;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 4px;
}
```
```tsx
import React from 'react';
import { Alert, Flex, Spin } from 'antd';

const App: React.FC = () => (
  <Flex gap="small" vertical>
    <Flex gap="small">
      <Spin tip="Loading" size="small">
        <div className="content" />
      </Spin>
      <Spin tip="Loading">
        <div className="content" />
      </Spin>
      <Spin tip="Loading" size="large">
        <div className="content" />
      </Spin>
    </Flex>
    <Spin tip="Loading...">
      <Alert
        message="Alert message title"
        description="Further details about the context of this alert."
        type="info"
      />
    </Spin>
  </Flex>
);

export default App;
```
