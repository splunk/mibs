#
# PySNMP MIB module CISCO-MAC-AUTH-BYPASS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MAC-AUTH-BYPASS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMacAuthBypassCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 574))
ciscoMacAuthBypassCapability.setRevisions(('2010-03-09 00:00', '2008-10-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setRevisionsDescriptions(('Added capability statement ciscoMabCapV12R0252SGPCat4K.\n\n        Added more VARIATION for ciscoMabCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setLastUpdated('201003090000Z')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n                E-mail: cs-ibns@cisco.com,\n                        cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoMacAuthBypassCapability.setDescription('The capabilities description of CISCO-MAC-AUTH-BYPASS-MIB.')
ciscoMabCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0233SXIPCat6K = ciscoMabCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoMabCapV12R0233SXIPCat6K.setDescription('CISCO-MAC-AUTH-BYPASS-MIB capabilities.')
ciscoMabCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 574, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMabCapV12R0252SGPCat4K = ciscoMabCapV12R0252SGPCat4K.setStatus('current')
if mibBuilder.loadTexts: ciscoMabCapV12R0252SGPCat4K.setDescription('CISCO-MAC-AUTH-BYPASS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MAC-AUTH-BYPASS-CAPABILITY", ciscoMacAuthBypassCapability=ciscoMacAuthBypassCapability, PYSNMP_MODULE_ID=ciscoMacAuthBypassCapability, ciscoMabCapV12R0233SXIPCat6K=ciscoMabCapV12R0233SXIPCat6K, ciscoMabCapV12R0252SGPCat4K=ciscoMabCapV12R0252SGPCat4K)
