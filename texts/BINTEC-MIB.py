#
# PySNMP MIB module BINTEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bintec/BINTEC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:05:53 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, enterprises, Counter64, ObjectIdentity, iso, TimeTicks, Integer32, Counter32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "enterprises", "Counter64", "ObjectIdentity", "iso", "TimeTicks", "Integer32", "Counter32", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
isdn = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 2))
biboip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
atm = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 16))
sys = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17))
admin_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 22)).setLabel("admin-2")
vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 23))
ipsec = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 26))
qos = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 27))
adsl = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 30))
voip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 33))
security = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 38))
vif = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 39))
tty = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 41))
ssh = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 44))
phy = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 45))
wlan = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 46))
ima = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 54))
usb = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 55))
resource = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17, 4))
gui = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 69))
class PhysAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Date(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class HexValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class BitValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("BINTEC-MIB", ipsec=ipsec, sys=sys, PhysAddress=PhysAddress, biboip=biboip, ima=ima, gui=gui, vif=vif, BitValue=BitValue, voip=voip, ssh=ssh, Date=Date, atm=atm, usb=usb, adsl=adsl, qos=qos, bibo=bibo, Timeout=Timeout, MacAddress=MacAddress, resource=resource, bintec=bintec, phy=phy, wlan=wlan, isdn=isdn, security=security, admin_2=admin_2, vpn=vpn, tty=tty, HexValue=HexValue, BridgeId=BridgeId, DisplayString=DisplayString)
