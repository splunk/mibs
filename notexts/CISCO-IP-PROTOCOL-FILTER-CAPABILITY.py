#
# PySNMP MIB module CISCO-IP-PROTOCOL-FILTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-PROTOCOL-FILTER-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
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
ciscoIpProtFilterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 500))
ciscoIpProtFilterCapability.setRevisions(('2008-06-09 00:00', '2006-04-19 00:00',))
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setLastUpdated('200806090000Z')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setOrganization('Cisco Systems, Inc.')
cIpProtFilterCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 500, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapACSWV03R000 = cIpProtFilterCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapACSWV03R000 = cIpProtFilterCapACSWV03R000.setStatus('current')
cIpProtFilterCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 500, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapc4710aceVA1R700 = cIpProtFilterCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                  for ACE 4710 Application Control Engine \n                  Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapc4710aceVA1R700 = cIpProtFilterCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-PROTOCOL-FILTER-CAPABILITY", cIpProtFilterCapACSWV03R000=cIpProtFilterCapACSWV03R000, ciscoIpProtFilterCapability=ciscoIpProtFilterCapability, PYSNMP_MODULE_ID=ciscoIpProtFilterCapability, cIpProtFilterCapc4710aceVA1R700=cIpProtFilterCapc4710aceVA1R700)
