#
# PySNMP MIB module CISCO-APPNAV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-APPNAV-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAppnavCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 610))
ciscoAppnavCapability.setRevisions(('2012-04-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAppnavCapability.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAppnavCapability.setLastUpdated('201204170000Z')
if mibBuilder.loadTexts: ciscoAppnavCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAppnavCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-<list>@cisco.com')
if mibBuilder.loadTexts: ciscoAppnavCapability.setDescription('Agent capabilities for CISCO-APPNAV-MIB.')
ciscoAppNavCapabilityWAASV5R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 610, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setProductRelease('OS=WAAS\n                     OSVERSION=V501')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setStatus('current')
if mibBuilder.loadTexts: ciscoAppNavCapabilityWAASV5R0.setDescription('CISCO-APPNAV-MIB capabilities')
mibBuilder.exportSymbols("CISCO-APPNAV-CAPABILITY", ciscoAppNavCapabilityWAASV5R0=ciscoAppNavCapabilityWAASV5R0, PYSNMP_MODULE_ID=ciscoAppnavCapability, ciscoAppnavCapability=ciscoAppnavCapability)
