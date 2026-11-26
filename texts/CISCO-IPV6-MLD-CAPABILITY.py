#
# PySNMP MIB module CISCO-IPV6-MLD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IPV6-MLD-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cipv6mldCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 470))
cipv6mldCapability.setRevisions(('2006-01-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cipv6mldCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cipv6mldCapability.setLastUpdated('200601070000Z')
if mibBuilder.loadTexts: cipv6mldCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cipv6mldCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com\n                        cs-snmp@cisco.com')
if mibBuilder.loadTexts: cipv6mldCapability.setDescription('The capabilities description of\n                 IPV6-MLD-MIB.')
ciscoIpv6MldCapCRS1V3R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 470, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6MldCapCRS1V3R02 = ciscoIpv6MldCapCRS1V3R02.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpv6MldCapCRS1V3R02 = ciscoIpv6MldCapCRS1V3R02.setStatus('current')
if mibBuilder.loadTexts: ciscoIpv6MldCapCRS1V3R02.setDescription('IPV6-MLD-MIB capabilities for\n                        IOS XR release 3.2.0')
mibBuilder.exportSymbols("CISCO-IPV6-MLD-CAPABILITY", PYSNMP_MODULE_ID=cipv6mldCapability, cipv6mldCapability=cipv6mldCapability, ciscoIpv6MldCapCRS1V3R02=ciscoIpv6MldCapCRS1V3R02)
