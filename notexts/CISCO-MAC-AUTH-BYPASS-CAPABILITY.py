#
# PySNMP MIB module CISCO-MAC-AUTH-BYPASS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MAC-AUTH-BYPASS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMacAuthBypassCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 574))
ciscoMacAuthBypassCapability.setRevisions(('2010-03-09 00:00', '2008-10-30 00:00',))
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setLastUpdated('201003090000Z')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setOrganization('Cisco Systems, Inc.')
ciscoMabCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setStatus('current')
ciscoMabCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAC-AUTH-BYPASS-CAPABILITY", PYSNMP_MODULE_ID=ciscoMacAuthBypassCapability, ciscoMacAuthBypassCapability=ciscoMacAuthBypassCapability, ciscoMabCapV12R0252SGPCat4K=ciscoMabCapV12R0252SGPCat4K, ciscoMabCapV12R0233SXIPCat6K=ciscoMabCapV12R0233SXIPCat6K)
