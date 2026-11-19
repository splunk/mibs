#
# PySNMP MIB module CISCO-ENTITY-DIAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-DIAG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEntityDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 529))
ciscoEntityDiagCapability.setRevisions(('2010-11-03 00:00', '2009-07-02 00:00', '2009-06-01 00:00', '2008-10-30 00:00', '2008-02-29 00:00', '2007-07-23 00:00', '2007-01-12 00:00',))
if mibBuilder.loadTexts: ciscoEntityDiagCapability.setLastUpdated('201011030000Z')
if mibBuilder.loadTexts: ciscoEntityDiagCapability.setOrganization('Cisco Systems, Inc.')
ceDiagCapCatOSV08R0601Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapCatOSV08R0601Cat6K = ceDiagCapCatOSV08R0601Cat6K.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500 series \n                     devices with Supervisor 720 or Supervisor 32 \n                     present.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapCatOSV08R0601Cat6K = ceDiagCapCatOSV08R0601Cat6K.setStatus('current')
ceDiagCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXHPCat6K = ceDiagCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXHPCat6K = ceDiagCapV12R0233SXHPCat6K.setStatus('current')
ceDiagCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXIPCat6K = ceDiagCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXIPCat6K = ceDiagCapV12R0233SXIPCat6K.setStatus('current')
ceDiagCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0252SGPCat4K = ceDiagCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on CAT4K family \n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0252SGPCat4K = ceDiagCapV12R0252SGPCat4K.setStatus('current')
ceDiagCapV12R0233SXI2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXI2PCat6K = ceDiagCapV12R0233SXI2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0233SXI2PCat6K = ceDiagCapV12R0233SXI2PCat6K.setStatus('current')
ceDiagCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 529, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0250SYPCat6K = ceDiagCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDiagCapV12R0250SYPCat6K = ceDiagCapV12R0250SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-DIAG-CAPABILITY", ceDiagCapV12R0233SXIPCat6K=ceDiagCapV12R0233SXIPCat6K, ceDiagCapV12R0233SXHPCat6K=ceDiagCapV12R0233SXHPCat6K, ceDiagCapV12R0250SYPCat6K=ceDiagCapV12R0250SYPCat6K, ciscoEntityDiagCapability=ciscoEntityDiagCapability, ceDiagCapV12R0233SXI2PCat6K=ceDiagCapV12R0233SXI2PCat6K, PYSNMP_MODULE_ID=ciscoEntityDiagCapability, ceDiagCapV12R0252SGPCat4K=ceDiagCapV12R0252SGPCat4K, ceDiagCapCatOSV08R0601Cat6K=ceDiagCapCatOSV08R0601Cat6K)
