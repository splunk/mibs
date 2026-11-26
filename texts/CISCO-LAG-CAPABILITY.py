#
# PySNMP MIB module CISCO-LAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LAG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 332))
ciscoLagCapability.setRevisions(('2012-04-02 00:00', '2011-09-27 00:00', '2010-11-01 00:00', '2009-11-19 00:00', '2007-07-10 10:00', '2006-06-15 12:00', '2004-02-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLagCapability.setRevisionsDescriptions(('Added capability statement clagCapV15R0101SGPCat4K.', 'Added capability statement clagCapV15R0001SYPCat6k.\n\n        Added VARIATION for clagAggDistributionProtocol object\n        in clagCapCatOSV08R0101 agent capabilty statement .', 'Added capability statement clagCapV12R0250SYPCat6K.', 'Added capability statement clagCapV12R0252SGPCat4K.', 'Added capability statement clagCapV12R0233SXHPCat6K.', 'Added capability statements\n        clagCapV12R0218SXF5PCat6KPfc2 and\n        clagCapV12R0218SXF5PCat6KPfc3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLagCapability.setLastUpdated('201204020000Z')
if mibBuilder.loadTexts: ciscoLagCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLagCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com,\n            cs-etherchan@cisco.com')
if mibBuilder.loadTexts: ciscoLagCapability.setDescription('The capabilities description of CISCO-LAG-MIB.')
clagCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0111bEXCat6K = clagCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0111bEXCat6K = clagCapV12R0111bEXCat6K.setStatus('current')
if mibBuilder.loadTexts: clagCapV12R0111bEXCat6K.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV12R0217SXCat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0217SXCat6KPfc2 = clagCapV12R0217SXCat6KPfc2.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                    and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0217SXCat6KPfc2 = clagCapV12R0217SXCat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: clagCapV12R0217SXCat6KPfc2.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV12R0217SXCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0217SXCat6KPfc3 = clagCapV12R0217SXCat6KPfc3.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                    and Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0217SXCat6KPfc3 = clagCapV12R0217SXCat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: clagCapV12R0217SXCat6KPfc3.setDescription('CISCO-LAG-MIB capabilities.')
clagCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapCatOSV08R0101 = clagCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapCatOSV08R0101 = clagCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: clagCapCatOSV08R0101.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV12R0218SXF5PCat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0218SXF5PCat6KPfc2 = clagCapV12R0218SXF5PCat6KPfc2.setProductRelease('Cisco IOS 12.2(18)SXF5 on Catalyst 6000/6500\n                    and Cisco 7600 series devices with PFC2 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0218SXF5PCat6KPfc2 = clagCapV12R0218SXF5PCat6KPfc2.setStatus('current')
if mibBuilder.loadTexts: clagCapV12R0218SXF5PCat6KPfc2.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV12R0218SXF5PCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0218SXF5PCat6KPfc3 = clagCapV12R0218SXF5PCat6KPfc3.setProductRelease('Cisco IOS 12.2(18)SXF5 on Catalyst 6000/6500\n                    and Cisco 7600 series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0218SXF5PCat6KPfc3 = clagCapV12R0218SXF5PCat6KPfc3.setStatus('current')
if mibBuilder.loadTexts: clagCapV12R0218SXF5PCat6KPfc3.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0233SXHPCat6K = clagCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0233SXHPCat6K = clagCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: clagCapV12R0233SXHPCat6K.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0252SGPCat4K = clagCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0252SGPCat4K = clagCapV12R0252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: clagCapV12R0252SGPCat4K.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0250SYPCat6K = clagCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV12R0250SYPCat6K = clagCapV12R0250SYPCat6K.setStatus('current')
if mibBuilder.loadTexts: clagCapV12R0250SYPCat6K.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV15R0001SYPCat6k = clagCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV15R0001SYPCat6k = clagCapV15R0001SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: clagCapV15R0001SYPCat6k.setDescription('CISCO-LAG-MIB capabilities.')
clagCapV15R0101SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 332, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV15R0101SGPCat4K = clagCapV15R0101SGPCat4K.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clagCapV15R0101SGPCat4K = clagCapV15R0101SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: clagCapV15R0101SGPCat4K.setDescription('CISCO-LAG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LAG-CAPABILITY", clagCapV15R0101SGPCat4K=clagCapV15R0101SGPCat4K, clagCapCatOSV08R0101=clagCapCatOSV08R0101, clagCapV12R0252SGPCat4K=clagCapV12R0252SGPCat4K, clagCapV12R0218SXF5PCat6KPfc3=clagCapV12R0218SXF5PCat6KPfc3, ciscoLagCapability=ciscoLagCapability, PYSNMP_MODULE_ID=ciscoLagCapability, clagCapV12R0233SXHPCat6K=clagCapV12R0233SXHPCat6K, clagCapV15R0001SYPCat6k=clagCapV15R0001SYPCat6k, clagCapV12R0217SXCat6KPfc2=clagCapV12R0217SXCat6KPfc2, clagCapV12R0218SXF5PCat6KPfc2=clagCapV12R0218SXF5PCat6KPfc2, clagCapV12R0111bEXCat6K=clagCapV12R0111bEXCat6K, clagCapV12R0217SXCat6KPfc3=clagCapV12R0217SXCat6KPfc3, clagCapV12R0250SYPCat6K=clagCapV12R0250SYPCat6K)
