#
# PySNMP MIB module CISCO-HW-MODULE-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-HW-MODULE-CONTROL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoHwModuleControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 588))
ciscoHwModuleControlCapability.setRevisions(('2012-09-07 00:00', '2011-09-27 00:00', '2010-03-17 00:00',))
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoHwModuleControlCapability.setOrganization('Cisco Systems, Inc.')
chmcCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV12R0233SXI4PCat6K = chmcCapV12R0233SXI4PCat6K.setStatus('current')
chmcCapV15R0001SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SYPCat6K = chmcCapV15R0001SYPCat6K.setStatus('current')
chmcCapV15R0001SY1PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 588, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setProductRelease('Cisco IOS 15.0(1)SY1 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chmcCapV15R0001SY1PCat6K = chmcCapV15R0001SY1PCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-HW-MODULE-CONTROL-CAPABILITY", PYSNMP_MODULE_ID=ciscoHwModuleControlCapability, chmcCapV15R0001SYPCat6K=chmcCapV15R0001SYPCat6K, chmcCapV12R0233SXI4PCat6K=chmcCapV12R0233SXI4PCat6K, chmcCapV15R0001SY1PCat6K=chmcCapV15R0001SY1PCat6K, ciscoHwModuleControlCapability=ciscoHwModuleControlCapability)
